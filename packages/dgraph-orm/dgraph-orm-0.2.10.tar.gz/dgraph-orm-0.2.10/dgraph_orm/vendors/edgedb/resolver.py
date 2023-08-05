import typing as T
from uuid import UUID
from enum import Enum
import re
import edgedb
from devtools import debug
from pydantic import BaseModel, PrivateAttr
from .execute import query as execute_query
from .node import Node
from .constants import ALIAS_PATTERN

NodeType = T.TypeVar("NodeType", bound=Node)

FILTER_FIELDS = ["_filter", "_limit", "_offset", "_order_by"]

ThisResolverType = T.TypeVar("ThisResolverType", bound="Resolver")


class ResolverException(Exception):
    pass


class UpdateOperation(str, Enum):
    """You can clear by choosing a resolver with REMOVE without filters"""

    REPLACE = ":="
    ADD = "+="
    REMOVE = "-="


class Resolver(BaseModel, T.Generic[NodeType]):
    """Can construct an EdgeQL query string from this!"""

    _node: T.ClassVar[T.Type[NodeType]]

    _filter: str = PrivateAttr(None)
    _order_by: str = PrivateAttr(None)
    _limit: int = PrivateAttr(None)
    _offset: int = PrivateAttr(None)
    _extra_fields: str = PrivateAttr(None)

    _modules: str = PrivateAttr(None)

    # this is just for updating
    _update_operation: UpdateOperation = PrivateAttr(None)

    _query_variables: T.Dict[str, T.Any] = PrivateAttr(default=dict())
    _nested_resolvers: T.Dict[str, "Resolver"] = PrivateAttr(default=dict())

    _fields_to_return: T.Set[str] = PrivateAttr(None)

    """PROPERTIES"""

    @classmethod
    @property
    def _model_name(cls) -> str:
        return cls._node._model_name

    def get_fields_to_return(self) -> T.Set[str]:
        """Include nested fields with DOT notation"""
        if self._fields_to_return is None:
            return set(self._node.__fields__.keys())
        return self._fields_to_return

    @property
    def _filter_str(self) -> str:
        if not self._filter:
            return ""
        return f"FILTER {self._filter}"

    @property
    def _order_by_str(self) -> str:
        if not self._order_by:
            return ""
        return f"ORDER BY {self._order_by}"

    @property
    def _limit_str(self) -> str:
        if not self._limit:
            return ""
        return f"LIMIT {self._limit}"

    @property
    def _offset_str(self) -> str:
        if not self._offset:
            return ""
        return f"OFFSET {self._offset}"

    @property
    def filters_to_dict(self) -> T.Dict[str, T.Any]:
        return {
            "filter": self._filter,
            "order by": self._order_by,
            "limit": self._limit,
            "offset": self._offset,
        }

    @property
    def update_operation_str(self) -> str:
        if not self._update_operation:
            return ""
        return self._update_operation.value

    """SETTERS"""

    def fields_to_return(
        self: ThisResolverType, fields_to_return: T.Set[str]
    ) -> ThisResolverType:
        self._fields_to_return = fields_to_return
        return self

    @staticmethod
    def validate_no_intersections_helper(
        set_a: T.Set = None, set_b: T.Set = None
    ) -> None:
        if set_a is None or set_b is None:
            return
        if used_keys := (set(set_a) & set(set_b)):
            raise ResolverException(
                f"Variable(s) {','.join(used_keys)} are already used."
            )

    def validate_against_query_variables(self, new_variables: dict = None) -> None:
        if not new_variables:
            return
        set_a = set(self._get_nested_query_variables().keys())
        set_b = set(new_variables.keys())
        self.validate_no_intersections_helper(set_a, set_b)

    def _add_variables(
        self, /, variables: T.Optional[T.Dict[str, T.Any]] = None
    ) -> None:
        if variables is not None:
            self.validate_against_query_variables(variables)
            self._query_variables = {**self._query_variables, **variables}

    def modules(self: ThisResolverType, module_str: str) -> ThisResolverType:
        if self._modules:
            raise ResolverException(
                f"Module of {self._modules} has already been provided."
            )
        self._modules = module_str
        return self

    def filter(
        self: ThisResolverType,
        filter_str: str,
        variables: T.Optional[T.Dict[str, T.Any]] = None,
    ) -> ThisResolverType:
        if self._filter:
            raise ResolverException(
                f"Filter of {self._filter} has already been provided."
            )
        # TODO change variable names
        self._add_variables(variables)
        self._filter = filter_str
        return self

    def extra_fields(
        self: ThisResolverType,
        extra_fields_str: str,
        variables: T.Optional[T.Dict[str, T.Any]] = None,
    ) -> ThisResolverType:
        if self._extra_fields:
            raise ResolverException(
                f"Extra fields of {self._extra_fields} has already been provided."
            )
        # TODO change variable names
        self._add_variables(variables)
        self._extra_fields = extra_fields_str
        return self

    def order_by(
        self: ThisResolverType,
        order_by_str: str,
        variables: T.Optional[T.Dict[str, T.Any]] = None,
    ) -> ThisResolverType:
        if self._order_by:
            raise ResolverException(
                f"Order by of {self._order_by} has already been provided."
            )
        self._add_variables(variables)
        self._order_by = order_by_str
        return self

    def limit(self: ThisResolverType, /, _: T.Optional[int]) -> ThisResolverType:
        if self._limit:
            raise ResolverException(
                f"Limit of {self._limit} has already been provided."
            )
        self._limit = _
        return self

    def offset(self: ThisResolverType, /, _: T.Optional[int]) -> ThisResolverType:
        if self._offset:
            raise ResolverException(
                f"Offset of {self._offset} has already been provided."
            )
        self._offset = _
        return self

    def update_operation(
        self: ThisResolverType, /, _: T.Optional[UpdateOperation]
    ) -> ThisResolverType:
        if self._update_operation:
            raise ResolverException(
                f"update_operation of {self._update_operation} has already been provided."
            )
        self._update_operation = _
        return self

    """QUERY STRING"""

    def _get_nested_query_variables(self) -> T.Dict[str, T.Any]:
        query_variables = {**self._query_variables}
        for nested_resolver in self._nested_resolvers.values():
            nested_query_variables = nested_resolver._get_nested_query_variables()
            if not nested_query_variables:
                continue
            if intersections := set(query_variables.keys()).intersection(
                set(nested_query_variables.keys())
            ):
                raise ResolverException(
                    f"'{', '.join(intersections)}' query value(s) used multiple times."
                )
            query_variables = {**query_variables, **nested_query_variables}
        return query_variables

    def all_filters_str(self) -> str:
        s = ""
        if self._filter:
            s += f" {self._filter_str}"
        if self._order_by:
            s += f" {self._order_by_str}"
        if self._offset:
            s += f" {self._offset_str}"
        if self._limit:
            s += f" {self._limit_str}"
        return s

    def to_str(self, include_filters: bool = True) -> str:
        """
        OUTPUT: { name, created_at, bookings: { created_at } FILTER .created_at > $booking_created_at } FILTER .name = $name }
        """
        s = ""
        s += ", ".join(self.get_fields_to_return())
        if self._extra_fields:
            s += f", {self._extra_fields}"
        resolver_strs: T.List[str] = []
        for field_name, resolver in self._nested_resolvers.items():
            resolver_substring = f"{field_name}: {resolver.to_str()}"
            resolver_strs.append(resolver_substring)
        nested_resolver_str = ", ".join(resolver_strs)
        if nested_resolver_str:
            s += f", {nested_resolver_str}"
        s = f"{{ {s} }}"
        if include_filters:
            s += self.all_filters_str()
        return s

    """HELPERS"""

    def has_filters(self) -> T.Optional[str]:
        for field in FILTER_FIELDS:
            if (val := getattr(self, field)) is not None:
                return val
        return None

    def clear_filters(self, remove_id_variable: bool = True) -> None:
        for field in FILTER_FIELDS:
            setattr(self, field, None)
        """Clearing filters does not clear query variables. 
        This is because you are only clearing the first level of filters."""
        if remove_id_variable:
            if "id" in self._query_variables:
                del self._query_variables["id"]

    """QUERY"""

    def full_query_str(self) -> str:
        module_str = "" if not self._modules else f"{self._modules} "
        return f"{module_str}SELECT {self._model_name} {self.to_str()}"

    def inner_delete_str(self) -> str:
        return f"DELETE {self._model_name} {self._filter_str}"

    def full_delete_str(self) -> str:
        return (
            f"WITH model := ({self.inner_delete_str()}) "
            f"SELECT model {self.to_str(include_filters=False)}"
        )

    async def query(
        self, given_client: edgedb.AsyncIOClient = None
    ) -> T.List[NodeType]:
        raw_d = await execute_query(
            client=given_client or self._node.db_client,
            query_str=self.full_query_str(),
            variables=self._get_nested_query_variables(),
        )
        return [self.parse_nested_obj(d) for d in raw_d]

    def clear_top_level_filters_and_variables(self) -> None:
        if self._filter:
            variables = re.findall(ALIAS_PATTERN, self._filter)
            for variable in variables:
                if variable in self._query_variables:
                    del self._query_variables[variable]
        self.clear_filters()

    async def get(
        self, given_client: edgedb.AsyncIOClient = None, **kwargs
    ) -> T.Optional[NodeType]:
        """Caveat is this must be a string value or an UUID"""
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        if len(kwargs) != 1:
            raise ResolverException(f"Must only give one argument, received {kwargs}")
        # if getting, make sure there are no filters attached to the resolver
        if existing_filter_str := self.has_filters():
            raise ResolverException(
                f"This resolver already has filters: {existing_filter_str}. "
                f"If you wish to GET an object, use a new resolver."
            )
        key, value = list(kwargs.items())[0]
        if key not in self._node._exclusive_fields:
            raise ResolverException(f"Field '{key}' is not exclusive.")
        # this is to avoid nested collisions
        variables = {key: value}
        if type(value) is UUID or key == "id":
            value_str = f"<uuid>${key}"
        elif type(value) is str or isinstance(value, Enum):
            # assume it is a string, can add if int or datetime i guess...
            value_str = f"<str>${key}"
        elif type(value) is int:
            value_str = f"<int16>${key}"
        else:
            value_str = value
            # need to test more: is this correct? Prob cause now using raw string given, no variables
            variables = {}
        self.filter(f".{key} = {value_str}", variables=variables)
        raw_d = await execute_query(
            client=given_client or self._node.db_client,
            query_str=self.full_query_str(),
            variables=self._get_nested_query_variables(),
            only_one=True,
        )
        if not raw_d:
            return None
        return self.parse_nested_obj(raw_d)

    async def gerror(self, **kwargs) -> NodeType:
        model = await self.get(**kwargs)
        if not model:
            raise ResolverException(f"No {self._model_name} in db with fields {kwargs}")
        return model

    def parse_nested_obj(
        self, raw_d: dict, error_for_extra_fields: bool = False
    ) -> NodeType:
        node: NodeType = self._node.parse_obj(raw_d)
        # pass on other fields as an "extra" dict
        other_fields = set(raw_d.keys()) - set(node.__fields__.keys())
        for field_name in other_fields:
            resolver: Resolver = self._nested_resolvers.get(field_name)
            if resolver is None:
                message = f"No nested resolver for {field_name=} found."
                if error_for_extra_fields:
                    raise ResolverException(message)
                node.extra[field_name] = raw_d[field_name]
                # print(message)
                continue
            nested_d = raw_d[field_name]
            value_to_save = nested_d
            if nested_d:
                if (list_or_set := type(nested_d)) in {list, set}:
                    val = list_or_set(resolver.parse_nested_obj(d) for d in nested_d)
                else:
                    val = resolver.parse_nested_obj(nested_d)
                value_to_save = val
            node.cache.add(
                key=field_name, resolver=resolver, val=value_to_save, raw_d=raw_d
            )
        node._used_resolver = self.copy(deep=True)
        node._original_dict = raw_d.copy()
        return node
