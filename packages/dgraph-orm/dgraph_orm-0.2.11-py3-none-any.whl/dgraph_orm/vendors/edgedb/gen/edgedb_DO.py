from __future__ import annotations
import typing as T
from enum import Enum
from datetime import datetime, date, timedelta
from uuid import UUID
from decimal import Decimal
from edgedb import RelativeDuration, AsyncIOClient, create_async_client
from pydantic import BaseModel, Field
from dgraph_orm.vendors.edgedb import (
    Node,
    Resolver,
    NodeException,
    ResolverException,
    UpdateOperation,
    Batch,
)

client = create_async_client(
    tls_security="insecure", host="143.244.174.160", password="beatgig8859", port=5656
)


class UserRole(str, Enum):
    buyer = "buyer"
    seller = "seller"
    admin = "admin"


class UserType(str, Enum):
    owner = "owner"
    employee = "employee"
    read_only = "read_only"
    Artist = "Artist"
    Agent = "Agent"
    Manager = "Manager"
    Other_Seller = "Other_Seller"
    Bar = "Bar"
    Brewery = "Brewery"
    Restaurant = "Restaurant"
    Nightclub = "Nightclub"
    Vineyard_Winery = "Vineyard_Winery"
    Theater = "Theater"
    Country_Club = "Country_Club"
    Hotel_Resort = "Hotel_Resort"
    University_Program_Board = "University_Program_Board"
    Fraternity_Sorority = "Fraternity_Sorority"
    Wedding = "Wedding"
    Corporate_Event = "Corporate_Event"
    Municipality = "Municipality"
    Other_Buyer = "Other_Buyer"


class VenueType(str, Enum):
    Bar = "Bar"
    Brewery = "Brewery"
    Restaurant = "Restaurant"
    Nightclub = "Nightclub"
    Municipality = "Municipality"
    Vineyard_Winery = "Vineyard_Winery"
    Theater = "Theater"
    Country_Club = "Country_Club"
    Other_Venue = "Other_Venue"
    Hotel = "Hotel"


class AnimalType(str, Enum):
    lion = "lion"
    tiger = "tiger"


class Category(str, Enum):
    Hip_Hop = "Hip_Hop"
    Pop = "Pop"
    EDM = "EDM"
    DJ = "DJ"
    Rock = "Rock"
    Country = "Country"
    Reggae = "Reggae"
    Jazz = "Jazz"
    Tribute = "Tribute"
    Comedy = "Comedy"


class BookingFlow(str, Enum):
    venue = "venue"
    private = "private"
    upb = "upb"


class IndoorsOrOutdoors(str, Enum):
    Indoors = "Indoors"
    Outdoors = "Outdoors"


class BookingStatus(str, Enum):
    created = "created"
    contracting = "contracting"
    negotiating = "negotiating"
    advancing = "advancing"
    performance = "performance"
    canceled = "canceled"
    declined = "declined"
    rescheduling = "rescheduling"


class BandConfigurationOption(str, Enum):
    solo = "solo"
    duo = "duo"
    trio = "trio"
    full_band = "full_band"


class Billing(str, Enum):
    Opener = "Opener"
    Headliner = "Headliner"
    Co_Headliner = "Co_Headliner"


class ArtistInsert(BaseModel):
    slug: str
    firebase_id: str
    created_at: datetime
    name: str
    connect_account_id: str
    last_updated: datetime
    published: bool
    media: T.Optional[str] = None
    admin_details: T.Optional[str] = None
    band_configuration: T.Optional[str] = None
    bio: T.Optional[str] = None
    category: T.Optional[Category] = None
    contact_information: T.Optional[str] = None
    cover_image: T.Optional[str] = None
    last_backend_updated: T.Optional[datetime] = None
    last_redis_refreshed: T.Optional[datetime] = None
    last_triggered_at: T.Optional[datetime] = None
    migration_version: T.Optional[int] = None
    profile_image: T.Optional[str] = None
    social_media: T.Optional[str] = None
    spotify_id: T.Optional[str] = None
    subgenres: T.Optional[T.List[str]] = None
    venue_take_percentages: T.Optional[str] = None
    version: T.Optional[int] = None
    sellers: T.Optional[UserResolver] = None
    bookings: T.Optional[BookingResolver] = None

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "slug": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "firebase_id": {"cast": "std::str", "cardinality": "One", "readonly": True},
        "created_at": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "name": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "connect_account_id": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "last_updated": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "published": {"cast": "std::bool", "cardinality": "One", "readonly": False},
        "media": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "admin_details": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "band_configuration": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "bio": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "category": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "contact_information": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "cover_image": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "last_backend_updated": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "last_redis_refreshed": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "last_triggered_at": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "migration_version": {
            "cast": "std::int16",
            "cardinality": "One",
            "readonly": False,
        },
        "profile_image": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "social_media": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "spotify_id": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "subgenres": {
            "cast": "array<std::str>",
            "cardinality": "One",
            "readonly": False,
        },
        "venue_take_percentages": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "version": {"cast": "std::int16", "cardinality": "One", "readonly": False},
    }


class Artist(Node[ArtistInsert]):
    id: UUID = Field(..., allow_mutation=False)
    slug: str = Field(..., allow_mutation=True)
    firebase_id: str = Field(..., allow_mutation=False)
    created_at: datetime = Field(..., allow_mutation=True)
    name: str = Field(..., allow_mutation=True)
    connect_account_id: str = Field(..., allow_mutation=True)
    last_updated: datetime = Field(..., allow_mutation=True)
    published: bool = Field(..., allow_mutation=True)
    media: T.Optional[str] = Field(None, allow_mutation=True)
    admin_details: T.Optional[str] = Field(None, allow_mutation=True)
    band_configuration: T.Optional[str] = Field(None, allow_mutation=True)
    bio: T.Optional[str] = Field(None, allow_mutation=True)
    category: T.Optional[Category] = Field(None, allow_mutation=True)
    contact_information: T.Optional[str] = Field(None, allow_mutation=True)
    cover_image: T.Optional[str] = Field(None, allow_mutation=True)
    last_backend_updated: T.Optional[datetime] = Field(None, allow_mutation=True)
    last_redis_refreshed: T.Optional[datetime] = Field(None, allow_mutation=True)
    last_triggered_at: T.Optional[datetime] = Field(None, allow_mutation=True)
    migration_version: T.Optional[int] = Field(None, allow_mutation=True)
    profile_image: T.Optional[str] = Field(None, allow_mutation=True)
    social_media: T.Optional[str] = Field(None, allow_mutation=True)
    spotify_id: T.Optional[str] = Field(None, allow_mutation=True)
    subgenres: T.Optional[T.List[str]] = Field(None, allow_mutation=True)
    venue_take_percentages: T.Optional[str] = Field(None, allow_mutation=True)
    version: T.Optional[int] = Field(None, allow_mutation=True)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": {"cast": "std::uuid", "cardinality": "One", "readonly": True},
        "slug": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "firebase_id": {"cast": "std::str", "cardinality": "One", "readonly": True},
        "created_at": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "name": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "connect_account_id": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "last_updated": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "published": {"cast": "std::bool", "cardinality": "One", "readonly": False},
        "media": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "admin_details": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "band_configuration": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "bio": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "category": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "contact_information": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "cover_image": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "last_backend_updated": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "last_redis_refreshed": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "last_triggered_at": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "migration_version": {
            "cast": "std::int16",
            "cardinality": "One",
            "readonly": False,
        },
        "profile_image": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "social_media": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "spotify_id": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "subgenres": {
            "cast": "array<std::str>",
            "cardinality": "One",
            "readonly": False,
        },
        "venue_take_percentages": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "version": {"cast": "std::int16", "cardinality": "One", "readonly": False},
    }
    _link_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "sellers": {
            "cast": "User",
            "cardinality": "Many",
            "readonly": False,
            "required": False,
        },
        "bookings": {
            "cast": "Booking",
            "cardinality": "Many",
            "readonly": False,
            "required": False,
        },
    }

    async def sellers(
        self,
        resolver: UserResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[User]]:
        return await self.resolve(
            edge_name="sellers",
            edge_resolver=resolver or UserResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def bookings(
        self,
        resolver: BookingResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[Booking]]:
        return await self.resolve(
            edge_name="bookings",
            edge_resolver=resolver or BookingResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def update(
        self,
        given_resolver: ArtistResolver = None,
        error_if_no_update: bool = False,
        batch: Batch = None,
        given_client: AsyncIOClient = None,
        sellers: T.Optional[UserResolver] = None,
        bookings: T.Optional[BookingResolver] = None,
    ) -> None:
        set_links_d = {"sellers": sellers, "bookings": bookings}
        set_links_d = {key: val for key, val in set_links_d.items() if val is not None}

        return await super().update(
            given_resolver=given_resolver,
            error_if_no_update=error_if_no_update,
            set_links_d=set_links_d,
            batch=batch,
            given_client=given_client,
        )

    class GraphORM:
        model_name = "Artist"
        client = client
        updatable_fields: T.Set[str] = {
            "admin_details",
            "band_configuration",
            "bio",
            "bookings",
            "category",
            "connect_account_id",
            "contact_information",
            "cover_image",
            "created_at",
            "last_backend_updated",
            "last_redis_refreshed",
            "last_triggered_at",
            "last_updated",
            "media",
            "migration_version",
            "name",
            "profile_image",
            "published",
            "sellers",
            "slug",
            "social_media",
            "spotify_id",
            "subgenres",
            "venue_take_percentages",
            "version",
        }
        exclusive_fields: T.Set[str] = {"firebase_id", "id", "slug"}


class ArtistResolver(Resolver[Artist]):
    _node = Artist

    def sellers(self, _: T.Optional[UserResolver] = None, /) -> ArtistResolver:
        if "sellers" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `sellers` has already been provided."
            )
        self._nested_resolvers["sellers"] = _ or UserResolver()
        return self

    def bookings(self, _: T.Optional[BookingResolver] = None, /) -> ArtistResolver:
        if "bookings" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `bookings` has already been provided."
            )
        self._nested_resolvers["bookings"] = _ or BookingResolver()
        return self


Artist.GraphORM.resolver_type = ArtistResolver


class UserInsert(BaseModel):
    phone_number: str
    slug: str
    firebase_id: str
    approved: bool
    email: str
    created_at: datetime
    name: str
    last_updated: datetime
    metadata: str
    user_role: UserRole
    user_type: UserType
    admin_permissions: T.Optional[T.List[str]] = None
    admin_type: T.Optional[UserType] = None
    approval: T.Optional[str] = None
    default_state_abbr: T.Optional[str] = None
    last_triggered_at: T.Optional[datetime] = None
    profile_image: T.Optional[str] = None
    referred_by_id: T.Optional[str] = None
    artists: T.Optional[ArtistResolver] = None
    venues: T.Optional[VenueResolver] = None
    venues_assigned_to: T.Optional[VenueResolver] = None
    account_exec_bookings: T.Optional[BookingResolver] = None
    bookings: T.Optional[BookingResolver] = None

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "phone_number": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "slug": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "firebase_id": {"cast": "std::str", "cardinality": "One", "readonly": True},
        "approved": {"cast": "std::bool", "cardinality": "One", "readonly": False},
        "email": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "created_at": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "name": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "last_updated": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "metadata": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "user_role": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "user_type": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "admin_permissions": {
            "cast": "array<std::str>",
            "cardinality": "One",
            "readonly": False,
        },
        "admin_type": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "approval": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "default_state_abbr": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "last_triggered_at": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "profile_image": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "referred_by_id": {"cast": "std::str", "cardinality": "One", "readonly": False},
    }


class User(Node[UserInsert]):
    id: UUID = Field(..., allow_mutation=False)
    phone_number: str = Field(..., allow_mutation=True)
    slug: str = Field(..., allow_mutation=True)
    firebase_id: str = Field(..., allow_mutation=False)
    approved: bool = Field(..., allow_mutation=True)
    email: str = Field(..., allow_mutation=True)
    created_at: datetime = Field(..., allow_mutation=True)
    name: str = Field(..., allow_mutation=True)
    last_updated: datetime = Field(..., allow_mutation=True)
    metadata: str = Field(..., allow_mutation=True)
    user_role: UserRole = Field(..., allow_mutation=True)
    user_type: UserType = Field(..., allow_mutation=True)
    admin_permissions: T.Optional[T.List[str]] = Field(None, allow_mutation=True)
    admin_type: T.Optional[UserType] = Field(None, allow_mutation=True)
    approval: T.Optional[str] = Field(None, allow_mutation=True)
    default_state_abbr: T.Optional[str] = Field(None, allow_mutation=True)
    last_triggered_at: T.Optional[datetime] = Field(None, allow_mutation=True)
    profile_image: T.Optional[str] = Field(None, allow_mutation=True)
    referred_by_id: T.Optional[str] = Field(None, allow_mutation=True)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": {"cast": "std::uuid", "cardinality": "One", "readonly": True},
        "phone_number": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "slug": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "firebase_id": {"cast": "std::str", "cardinality": "One", "readonly": True},
        "approved": {"cast": "std::bool", "cardinality": "One", "readonly": False},
        "email": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "created_at": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "name": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "last_updated": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "metadata": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "user_role": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "user_type": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "admin_permissions": {
            "cast": "array<std::str>",
            "cardinality": "One",
            "readonly": False,
        },
        "admin_type": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "approval": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "default_state_abbr": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "last_triggered_at": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "profile_image": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "referred_by_id": {"cast": "std::str", "cardinality": "One", "readonly": False},
    }
    _link_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "artists": {
            "cast": "Artist",
            "cardinality": "Many",
            "readonly": False,
            "required": False,
        },
        "venues": {
            "cast": "Venue",
            "cardinality": "Many",
            "readonly": False,
            "required": False,
        },
        "venues_assigned_to": {
            "cast": "Venue",
            "cardinality": "Many",
            "readonly": False,
            "required": False,
        },
        "account_exec_bookings": {
            "cast": "Booking",
            "cardinality": "Many",
            "readonly": False,
            "required": False,
        },
        "bookings": {
            "cast": "Booking",
            "cardinality": "Many",
            "readonly": False,
            "required": False,
        },
    }

    async def artists(
        self,
        resolver: ArtistResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[Artist]]:
        return await self.resolve(
            edge_name="artists",
            edge_resolver=resolver or ArtistResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def venues(
        self,
        resolver: VenueResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[Venue]]:
        return await self.resolve(
            edge_name="venues",
            edge_resolver=resolver or VenueResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def venues_assigned_to(
        self,
        resolver: VenueResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[Venue]]:
        return await self.resolve(
            edge_name="venues_assigned_to",
            edge_resolver=resolver or VenueResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def account_exec_bookings(
        self,
        resolver: BookingResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[Booking]]:
        return await self.resolve(
            edge_name="account_exec_bookings",
            edge_resolver=resolver or BookingResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def bookings(
        self,
        resolver: BookingResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[Booking]]:
        return await self.resolve(
            edge_name="bookings",
            edge_resolver=resolver or BookingResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def update(
        self,
        given_resolver: UserResolver = None,
        error_if_no_update: bool = False,
        batch: Batch = None,
        given_client: AsyncIOClient = None,
        artists: T.Optional[ArtistResolver] = None,
        venues: T.Optional[VenueResolver] = None,
        venues_assigned_to: T.Optional[VenueResolver] = None,
        account_exec_bookings: T.Optional[BookingResolver] = None,
        bookings: T.Optional[BookingResolver] = None,
    ) -> None:
        set_links_d = {
            "artists": artists,
            "venues": venues,
            "venues_assigned_to": venues_assigned_to,
            "account_exec_bookings": account_exec_bookings,
            "bookings": bookings,
        }
        set_links_d = {key: val for key, val in set_links_d.items() if val is not None}

        return await super().update(
            given_resolver=given_resolver,
            error_if_no_update=error_if_no_update,
            set_links_d=set_links_d,
            batch=batch,
            given_client=given_client,
        )

    class GraphORM:
        model_name = "User"
        client = client
        updatable_fields: T.Set[str] = {
            "account_exec_bookings",
            "admin_permissions",
            "admin_type",
            "approval",
            "approved",
            "artists",
            "bookings",
            "created_at",
            "default_state_abbr",
            "email",
            "last_triggered_at",
            "last_updated",
            "metadata",
            "name",
            "phone_number",
            "profile_image",
            "referred_by_id",
            "slug",
            "user_role",
            "user_type",
            "venues",
            "venues_assigned_to",
        }
        exclusive_fields: T.Set[str] = {"firebase_id", "id", "phone_number", "slug"}


class UserResolver(Resolver[User]):
    _node = User

    def artists(self, _: T.Optional[ArtistResolver] = None, /) -> UserResolver:
        if "artists" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `artists` has already been provided."
            )
        self._nested_resolvers["artists"] = _ or ArtistResolver()
        return self

    def venues(self, _: T.Optional[VenueResolver] = None, /) -> UserResolver:
        if "venues" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `venues` has already been provided."
            )
        self._nested_resolvers["venues"] = _ or VenueResolver()
        return self

    def venues_assigned_to(
        self, _: T.Optional[VenueResolver] = None, /
    ) -> UserResolver:
        if "venues_assigned_to" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `venues_assigned_to` has already been provided."
            )
        self._nested_resolvers["venues_assigned_to"] = _ or VenueResolver()
        return self

    def account_exec_bookings(
        self, _: T.Optional[BookingResolver] = None, /
    ) -> UserResolver:
        if "account_exec_bookings" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `account_exec_bookings` has already been provided."
            )
        self._nested_resolvers["account_exec_bookings"] = _ or BookingResolver()
        return self

    def bookings(self, _: T.Optional[BookingResolver] = None, /) -> UserResolver:
        if "bookings" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `bookings` has already been provided."
            )
        self._nested_resolvers["bookings"] = _ or BookingResolver()
        return self


User.GraphORM.resolver_type = UserResolver


class MovieInsert(BaseModel):
    title: str
    year: T.Optional[int] = None
    actors: T.Optional[PersonResolver] = None
    director: T.Optional[PersonResolver] = None

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "title": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "year": {"cast": "std::int64", "cardinality": "One", "readonly": False},
    }


class Movie(Node[MovieInsert]):
    id: UUID = Field(..., allow_mutation=False)
    title: str = Field(..., allow_mutation=True)
    year: T.Optional[int] = Field(None, allow_mutation=True)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": {"cast": "std::uuid", "cardinality": "One", "readonly": True},
        "title": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "year": {"cast": "std::int64", "cardinality": "One", "readonly": False},
    }
    _link_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "actors": {
            "cast": "Person",
            "cardinality": "Many",
            "readonly": False,
            "required": False,
        },
        "director": {
            "cast": "Person",
            "cardinality": "One",
            "readonly": False,
            "required": False,
        },
    }

    async def actors(
        self,
        resolver: PersonResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[Person]]:
        return await self.resolve(
            edge_name="actors",
            edge_resolver=resolver or PersonResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def director(
        self,
        resolver: PersonResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[Person]:
        return await self.resolve(
            edge_name="director",
            edge_resolver=resolver or PersonResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def update(
        self,
        given_resolver: MovieResolver = None,
        error_if_no_update: bool = False,
        batch: Batch = None,
        given_client: AsyncIOClient = None,
        actors: T.Optional[PersonResolver] = None,
        director: T.Optional[PersonResolver] = None,
    ) -> None:
        set_links_d = {"actors": actors, "director": director}
        set_links_d = {key: val for key, val in set_links_d.items() if val is not None}

        return await super().update(
            given_resolver=given_resolver,
            error_if_no_update=error_if_no_update,
            set_links_d=set_links_d,
            batch=batch,
            given_client=given_client,
        )

    class GraphORM:
        model_name = "Movie"
        client = client
        updatable_fields: T.Set[str] = {"actors", "director", "title", "year"}
        exclusive_fields: T.Set[str] = {"id"}


class MovieResolver(Resolver[Movie]):
    _node = Movie

    def actors(self, _: T.Optional[PersonResolver] = None, /) -> MovieResolver:
        if "actors" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `actors` has already been provided."
            )
        self._nested_resolvers["actors"] = _ or PersonResolver()
        return self

    def director(self, _: T.Optional[PersonResolver] = None, /) -> MovieResolver:
        if "director" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `director` has already been provided."
            )
        self._nested_resolvers["director"] = _ or PersonResolver()
        return self


Movie.GraphORM.resolver_type = MovieResolver


class PersonInsert(BaseModel):
    slug: str
    # inserted_at: T.Optional[datetime] = None
    first_name: str
    last_name: T.Optional[str] = None
    # full_name: T.Optional[str] = None
    tags: T.Optional[T.Set[str]] = None
    ordered_tags: T.Optional[T.List[str]] = None
    created_at: T.Optional[datetime] = None
    # my_followers: T.Optional[PersonResolver] = None
    best_friend: T.Optional[PersonResolver] = None
    people_i_follow: T.Optional[PersonResolver] = None

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "slug": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "inserted_at": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": True,
        },
        "first_name": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "last_name": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "full_name": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "tags": {"cast": "std::str", "cardinality": "Many", "readonly": False},
        "ordered_tags": {
            "cast": "array<std::str>",
            "cardinality": "One",
            "readonly": False,
        },
        "created_at": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
    }


class Person(Node[PersonInsert]):
    id: UUID = Field(..., allow_mutation=False)
    slug: str = Field(..., allow_mutation=True)
    inserted_at: datetime = Field(..., allow_mutation=False)
    first_name: str = Field(..., allow_mutation=True)
    last_name: T.Optional[str] = Field(None, allow_mutation=True)
    full_name: T.Optional[str] = Field(None, allow_mutation=True)
    tags: T.Optional[T.Set[str]] = Field(None, allow_mutation=True)
    ordered_tags: T.Optional[T.List[str]] = Field(None, allow_mutation=True)
    created_at: T.Optional[datetime] = Field(None, allow_mutation=True)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": {"cast": "std::uuid", "cardinality": "One", "readonly": True},
        "slug": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "inserted_at": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": True,
        },
        "first_name": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "last_name": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "full_name": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "tags": {"cast": "std::str", "cardinality": "Many", "readonly": False},
        "ordered_tags": {
            "cast": "array<std::str>",
            "cardinality": "One",
            "readonly": False,
        },
        "created_at": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
    }
    _link_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "my_followers": {
            "cast": "Person",
            "cardinality": "Many",
            "readonly": False,
            "required": False,
        },
        "best_friend": {
            "cast": "Person",
            "cardinality": "One",
            "readonly": False,
            "required": False,
        },
        "people_i_follow": {
            "cast": "Person",
            "cardinality": "Many",
            "readonly": False,
            "required": False,
        },
    }

    async def my_followers(
        self,
        resolver: PersonResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[Person]]:
        return await self.resolve(
            edge_name="my_followers",
            edge_resolver=resolver or PersonResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def best_friend(
        self,
        resolver: PersonResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[Person]:
        return await self.resolve(
            edge_name="best_friend",
            edge_resolver=resolver or PersonResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def people_i_follow(
        self,
        resolver: PersonResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[Person]]:
        return await self.resolve(
            edge_name="people_i_follow",
            edge_resolver=resolver or PersonResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def update(
        self,
        given_resolver: PersonResolver = None,
        error_if_no_update: bool = False,
        batch: Batch = None,
        given_client: AsyncIOClient = None,
        my_followers: T.Optional[PersonResolver] = None,
        best_friend: T.Optional[PersonResolver] = None,
        people_i_follow: T.Optional[PersonResolver] = None,
    ) -> None:
        set_links_d = {
            "my_followers": my_followers,
            "best_friend": best_friend,
            "people_i_follow": people_i_follow,
        }
        set_links_d = {key: val for key, val in set_links_d.items() if val is not None}

        return await super().update(
            given_resolver=given_resolver,
            error_if_no_update=error_if_no_update,
            set_links_d=set_links_d,
            batch=batch,
            given_client=given_client,
        )

    class GraphORM:
        model_name = "Person"
        client = client
        updatable_fields: T.Set[str] = {
            "best_friend",
            "created_at",
            "first_name",
            # "full_name",
            "last_name",
            "my_followers",
            "ordered_tags",
            "people_i_follow",
            "slug",
            "tags",
        }
        exclusive_fields: T.Set[str] = {"id", "slug"}


class PersonResolver(Resolver[Person]):
    _node = Person

    def my_followers(self, _: T.Optional[PersonResolver] = None, /) -> PersonResolver:
        if "my_followers" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `my_followers` has already been provided."
            )
        self._nested_resolvers["my_followers"] = _ or PersonResolver()
        return self

    def best_friend(self, _: T.Optional[PersonResolver] = None, /) -> PersonResolver:
        if "best_friend" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `best_friend` has already been provided."
            )
        self._nested_resolvers["best_friend"] = _ or PersonResolver()
        return self

    def people_i_follow(
        self, _: T.Optional[PersonResolver] = None, /
    ) -> PersonResolver:
        if "people_i_follow" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `people_i_follow` has already been provided."
            )
        self._nested_resolvers["people_i_follow"] = _ or PersonResolver()
        return self


Person.GraphORM.resolver_type = PersonResolver


class VenueInsert(BaseModel):
    slug: str
    firebase_id: str
    created_at: datetime
    customer_id: str
    last_updated: datetime
    location: str
    name: str
    num_stages: int
    place_id: str
    venue_type: VenueType
    budget: T.Optional[str] = None
    capacity: T.Optional[int] = None
    colors: T.Optional[str] = None
    display_images: T.Optional[str] = None
    genres_booked: T.Optional[T.List[str]] = None
    images: T.Optional[str] = None
    logo: T.Optional[str] = None
    phone_number: T.Optional[str] = None
    production_and_venue_specs: T.Optional[str] = None
    social_media: T.Optional[str] = None
    website: T.Optional[str] = None
    created_by: UserResolver
    account_exec: T.Optional[UserResolver] = None
    owners: T.Optional[UserResolver] = None
    bookings: T.Optional[BookingResolver] = None
    external_bookings: T.Optional[ExternalBookingResolver] = None

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "slug": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "firebase_id": {"cast": "std::str", "cardinality": "One", "readonly": True},
        "created_at": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "customer_id": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "last_updated": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "location": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "name": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "num_stages": {"cast": "std::int16", "cardinality": "One", "readonly": False},
        "place_id": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "venue_type": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "budget": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "capacity": {"cast": "std::int16", "cardinality": "One", "readonly": False},
        "colors": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "display_images": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "genres_booked": {
            "cast": "array<std::str>",
            "cardinality": "One",
            "readonly": False,
        },
        "images": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "logo": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "phone_number": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "production_and_venue_specs": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "social_media": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "website": {"cast": "std::str", "cardinality": "One", "readonly": False},
    }


class Venue(Node[VenueInsert]):
    id: UUID = Field(..., allow_mutation=False)
    slug: str = Field(..., allow_mutation=True)
    firebase_id: str = Field(..., allow_mutation=False)
    created_at: datetime = Field(..., allow_mutation=True)
    customer_id: str = Field(..., allow_mutation=True)
    last_updated: datetime = Field(..., allow_mutation=True)
    location: str = Field(..., allow_mutation=True)
    name: str = Field(..., allow_mutation=True)
    num_stages: int = Field(..., allow_mutation=True)
    place_id: str = Field(..., allow_mutation=True)
    venue_type: VenueType = Field(..., allow_mutation=True)
    budget: T.Optional[str] = Field(None, allow_mutation=True)
    capacity: T.Optional[int] = Field(None, allow_mutation=True)
    colors: T.Optional[str] = Field(None, allow_mutation=True)
    display_images: T.Optional[str] = Field(None, allow_mutation=True)
    genres_booked: T.Optional[T.List[str]] = Field(None, allow_mutation=True)
    images: T.Optional[str] = Field(None, allow_mutation=True)
    logo: T.Optional[str] = Field(None, allow_mutation=True)
    phone_number: T.Optional[str] = Field(None, allow_mutation=True)
    production_and_venue_specs: T.Optional[str] = Field(None, allow_mutation=True)
    social_media: T.Optional[str] = Field(None, allow_mutation=True)
    website: T.Optional[str] = Field(None, allow_mutation=True)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": {"cast": "std::uuid", "cardinality": "One", "readonly": True},
        "slug": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "firebase_id": {"cast": "std::str", "cardinality": "One", "readonly": True},
        "created_at": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "customer_id": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "last_updated": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "location": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "name": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "num_stages": {"cast": "std::int16", "cardinality": "One", "readonly": False},
        "place_id": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "venue_type": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "budget": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "capacity": {"cast": "std::int16", "cardinality": "One", "readonly": False},
        "colors": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "display_images": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "genres_booked": {
            "cast": "array<std::str>",
            "cardinality": "One",
            "readonly": False,
        },
        "images": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "logo": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "phone_number": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "production_and_venue_specs": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "social_media": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "website": {"cast": "std::str", "cardinality": "One", "readonly": False},
    }
    _link_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "created_by": {
            "cast": "User",
            "cardinality": "One",
            "readonly": False,
            "required": True,
        },
        "account_exec": {
            "cast": "User",
            "cardinality": "One",
            "readonly": False,
            "required": False,
        },
        "owners": {
            "cast": "User",
            "cardinality": "Many",
            "readonly": False,
            "required": False,
        },
        "bookings": {
            "cast": "Booking",
            "cardinality": "Many",
            "readonly": False,
            "required": False,
        },
        "external_bookings": {
            "cast": "ExternalBooking",
            "cardinality": "Many",
            "readonly": False,
            "required": False,
        },
    }

    async def created_by(
        self,
        resolver: UserResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> User:
        return await self.resolve(
            edge_name="created_by",
            edge_resolver=resolver or UserResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def account_exec(
        self,
        resolver: UserResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[User]:
        return await self.resolve(
            edge_name="account_exec",
            edge_resolver=resolver or UserResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def owners(
        self,
        resolver: UserResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[User]]:
        return await self.resolve(
            edge_name="owners",
            edge_resolver=resolver or UserResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def bookings(
        self,
        resolver: BookingResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[Booking]]:
        return await self.resolve(
            edge_name="bookings",
            edge_resolver=resolver or BookingResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def external_bookings(
        self,
        resolver: ExternalBookingResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[T.List[ExternalBooking]]:
        return await self.resolve(
            edge_name="external_bookings",
            edge_resolver=resolver or ExternalBookingResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def update(
        self,
        given_resolver: VenueResolver = None,
        error_if_no_update: bool = False,
        batch: Batch = None,
        given_client: AsyncIOClient = None,
        created_by: T.Optional[UserResolver] = None,
        account_exec: T.Optional[UserResolver] = None,
        owners: T.Optional[UserResolver] = None,
        bookings: T.Optional[BookingResolver] = None,
        external_bookings: T.Optional[ExternalBookingResolver] = None,
    ) -> None:
        set_links_d = {
            "created_by": created_by,
            "account_exec": account_exec,
            "owners": owners,
            "bookings": bookings,
            "external_bookings": external_bookings,
        }
        set_links_d = {key: val for key, val in set_links_d.items() if val is not None}

        return await super().update(
            given_resolver=given_resolver,
            error_if_no_update=error_if_no_update,
            set_links_d=set_links_d,
            batch=batch,
            given_client=given_client,
        )

    class GraphORM:
        model_name = "Venue"
        client = client
        updatable_fields: T.Set[str] = {
            "account_exec",
            "bookings",
            "budget",
            "capacity",
            "colors",
            "created_at",
            "created_by",
            "customer_id",
            "display_images",
            "external_bookings",
            "genres_booked",
            "images",
            "last_updated",
            "location",
            "logo",
            "name",
            "num_stages",
            "owners",
            "phone_number",
            "place_id",
            "production_and_venue_specs",
            "slug",
            "social_media",
            "venue_type",
            "website",
        }
        exclusive_fields: T.Set[str] = {"firebase_id", "id", "slug"}


class VenueResolver(Resolver[Venue]):
    _node = Venue

    def created_by(self, _: T.Optional[UserResolver] = None, /) -> VenueResolver:
        if "created_by" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `created_by` has already been provided."
            )
        self._nested_resolvers["created_by"] = _ or UserResolver()
        return self

    def account_exec(self, _: T.Optional[UserResolver] = None, /) -> VenueResolver:
        if "account_exec" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `account_exec` has already been provided."
            )
        self._nested_resolvers["account_exec"] = _ or UserResolver()
        return self

    def owners(self, _: T.Optional[UserResolver] = None, /) -> VenueResolver:
        if "owners" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `owners` has already been provided."
            )
        self._nested_resolvers["owners"] = _ or UserResolver()
        return self

    def bookings(self, _: T.Optional[BookingResolver] = None, /) -> VenueResolver:
        if "bookings" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `bookings` has already been provided."
            )
        self._nested_resolvers["bookings"] = _ or BookingResolver()
        return self

    def external_bookings(
        self, _: T.Optional[ExternalBookingResolver] = None, /
    ) -> VenueResolver:
        if "external_bookings" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `external_bookings` has already been provided."
            )
        self._nested_resolvers["external_bookings"] = _ or ExternalBookingResolver()
        return self


Venue.GraphORM.resolver_type = VenueResolver


class AnimalInsert(BaseModel):
    public_id: str
    slug: str
    name: str
    animal_type: AnimalType
    description: T.Optional[str] = None
    age: T.Optional[int] = None
    created_at: T.Optional[datetime] = None

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "public_id": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "slug": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "name": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "animal_type": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "description": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "age": {"cast": "std::int16", "cardinality": "One", "readonly": False},
        "created_at": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
    }


class Animal(Node[AnimalInsert]):
    id: UUID = Field(..., allow_mutation=False)
    public_id: str = Field(..., allow_mutation=True)
    slug: str = Field(..., allow_mutation=True)
    name: str = Field(..., allow_mutation=True)
    animal_type: AnimalType = Field(..., allow_mutation=True)
    description: T.Optional[str] = Field(None, allow_mutation=True)
    age: T.Optional[int] = Field(None, allow_mutation=True)
    created_at: T.Optional[datetime] = Field(None, allow_mutation=True)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": {"cast": "std::uuid", "cardinality": "One", "readonly": True},
        "public_id": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "slug": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "name": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "animal_type": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "description": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "age": {"cast": "std::int16", "cardinality": "One", "readonly": False},
        "created_at": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
    }
    _link_conversion_map: T.ClassVar[T.Dict[str, str]] = {}

    async def update(
        self,
        given_resolver: AnimalResolver = None,
        error_if_no_update: bool = False,
        batch: Batch = None,
        given_client: AsyncIOClient = None,
    ) -> None:
        set_links_d = {}
        set_links_d = {key: val for key, val in set_links_d.items() if val is not None}

        return await super().update(
            given_resolver=given_resolver,
            error_if_no_update=error_if_no_update,
            set_links_d=set_links_d,
            batch=batch,
            given_client=given_client,
        )

    class GraphORM:
        model_name = "Animal"
        client = client
        updatable_fields: T.Set[str] = {
            "age",
            "animal_type",
            "created_at",
            "description",
            "name",
            "public_id",
            "slug",
        }
        exclusive_fields: T.Set[str] = {"id", "public_id", "slug"}


class AnimalResolver(Resolver[Animal]):
    _node = Animal


Animal.GraphORM.resolver_type = AnimalResolver


class FirebaseObjectInsert(BaseModel):
    firebase_id: str

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "firebase_id": {"cast": "std::str", "cardinality": "One", "readonly": True}
    }


class FirebaseObject(Node[FirebaseObjectInsert]):
    id: UUID = Field(..., allow_mutation=False)
    firebase_id: str = Field(..., allow_mutation=False)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": {"cast": "std::uuid", "cardinality": "One", "readonly": True},
        "firebase_id": {"cast": "std::str", "cardinality": "One", "readonly": True},
    }
    _link_conversion_map: T.ClassVar[T.Dict[str, str]] = {}

    async def update(
        self,
        given_resolver: FirebaseObjectResolver = None,
        error_if_no_update: bool = False,
        batch: Batch = None,
        given_client: AsyncIOClient = None,
    ) -> None:
        set_links_d = {}
        set_links_d = {key: val for key, val in set_links_d.items() if val is not None}

        return await super().update(
            given_resolver=given_resolver,
            error_if_no_update=error_if_no_update,
            set_links_d=set_links_d,
            batch=batch,
            given_client=given_client,
        )

    class GraphORM:
        model_name = "FirebaseObject"
        client = client
        updatable_fields: T.Set[str] = {}
        exclusive_fields: T.Set[str] = {"firebase_id", "id"}


class FirebaseObjectResolver(Resolver[FirebaseObject]):
    _node = FirebaseObject


FirebaseObject.GraphORM.resolver_type = FirebaseObjectResolver


class MetaBookingInsert(BaseModel):
    firebase_id: str
    performance_length_mins: int
    start_time: datetime
    is_published: bool
    indoors_or_outdoors: T.Optional[IndoorsOrOutdoors] = None
    public_event_description: T.Optional[str] = None
    venue: T.Optional[VenueResolver] = None

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "firebase_id": {"cast": "std::str", "cardinality": "One", "readonly": True},
        "performance_length_mins": {
            "cast": "std::int16",
            "cardinality": "One",
            "readonly": False,
        },
        "start_time": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "is_published": {"cast": "std::bool", "cardinality": "One", "readonly": False},
        "indoors_or_outdoors": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "public_event_description": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
    }


class MetaBooking(Node[MetaBookingInsert]):
    id: UUID = Field(..., allow_mutation=False)
    firebase_id: str = Field(..., allow_mutation=False)
    performance_length_mins: int = Field(..., allow_mutation=True)
    start_time: datetime = Field(..., allow_mutation=True)
    is_published: bool = Field(..., allow_mutation=True)
    indoors_or_outdoors: T.Optional[IndoorsOrOutdoors] = Field(
        None, allow_mutation=True
    )
    public_event_description: T.Optional[str] = Field(None, allow_mutation=True)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": {"cast": "std::uuid", "cardinality": "One", "readonly": True},
        "firebase_id": {"cast": "std::str", "cardinality": "One", "readonly": True},
        "performance_length_mins": {
            "cast": "std::int16",
            "cardinality": "One",
            "readonly": False,
        },
        "start_time": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "is_published": {"cast": "std::bool", "cardinality": "One", "readonly": False},
        "indoors_or_outdoors": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "public_event_description": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
    }
    _link_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "venue": {
            "cast": "Venue",
            "cardinality": "One",
            "readonly": False,
            "required": False,
        }
    }

    async def venue(
        self,
        resolver: VenueResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[Venue]:
        return await self.resolve(
            edge_name="venue",
            edge_resolver=resolver or VenueResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def update(
        self,
        given_resolver: MetaBookingResolver = None,
        error_if_no_update: bool = False,
        batch: Batch = None,
        given_client: AsyncIOClient = None,
        venue: T.Optional[VenueResolver] = None,
    ) -> None:
        set_links_d = {"venue": venue}
        set_links_d = {key: val for key, val in set_links_d.items() if val is not None}

        return await super().update(
            given_resolver=given_resolver,
            error_if_no_update=error_if_no_update,
            set_links_d=set_links_d,
            batch=batch,
            given_client=given_client,
        )

    class GraphORM:
        model_name = "MetaBooking"
        client = client
        updatable_fields: T.Set[str] = {
            "indoors_or_outdoors",
            "is_published",
            "performance_length_mins",
            "public_event_description",
            "start_time",
            "venue",
        }
        exclusive_fields: T.Set[str] = {"firebase_id", "id"}


class MetaBookingResolver(Resolver[MetaBooking]):
    _node = MetaBooking

    def venue(self, _: T.Optional[VenueResolver] = None, /) -> MetaBookingResolver:
        if "venue" in self._nested_resolvers:
            raise ResolverException("A resolver for `venue` has already been provided.")
        self._nested_resolvers["venue"] = _ or VenueResolver()
        return self


MetaBooking.GraphORM.resolver_type = MetaBookingResolver


class BookingInsert(BaseModel):
    firebase_id: str
    performance_length_mins: int
    start_time: datetime
    created_at: datetime
    booking_flow: BookingFlow
    location: str
    negotiation_steps: str
    status: BookingStatus
    is_published: bool
    indoors_or_outdoors: T.Optional[IndoorsOrOutdoors] = None
    public_event_description: T.Optional[str] = None
    admin_cancellation_message: T.Optional[str] = None
    band_configuration: T.Optional[BandConfigurationOption] = None
    booking_dispute: T.Optional[str] = None
    buyer_has_reviewed: T.Optional[bool] = None
    charge: T.Optional[str] = None
    comments: T.Optional[str] = None
    customer_balance_transaction_id: T.Optional[str] = None
    deposit: T.Optional[str] = None
    last_triggered_at: T.Optional[datetime] = None
    last_updated: T.Optional[datetime] = None
    old_start_time: T.Optional[datetime] = None
    payout: T.Optional[str] = None
    production_and_venue_specs: T.Optional[str] = None
    refunded_in_credits: T.Optional[bool] = None
    reschedule_message: T.Optional[str] = None
    resolved_booking_dispute: T.Optional[str] = None
    seller_has_reviewed: T.Optional[bool] = None
    should_auto_publish: T.Optional[bool] = None
    week_out_notification_at: T.Optional[datetime] = None
    billing: T.Optional[Billing] = None
    week_out_notification: T.Optional[bool] = None
    capacity: T.Optional[int] = None
    has_extra_charge: T.Optional[bool] = None
    has_extra_payout: T.Optional[bool] = None
    artist: ArtistResolver
    buyer: UserResolver
    account_exec: T.Optional[UserResolver] = None
    venue: T.Optional[VenueResolver] = None

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "firebase_id": {"cast": "std::str", "cardinality": "One", "readonly": True},
        "performance_length_mins": {
            "cast": "std::int16",
            "cardinality": "One",
            "readonly": False,
        },
        "start_time": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "created_at": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "booking_flow": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "location": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "negotiation_steps": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "status": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "is_published": {"cast": "std::bool", "cardinality": "One", "readonly": False},
        "indoors_or_outdoors": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "public_event_description": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "admin_cancellation_message": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "band_configuration": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "booking_dispute": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "buyer_has_reviewed": {
            "cast": "std::bool",
            "cardinality": "One",
            "readonly": False,
        },
        "charge": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "comments": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "customer_balance_transaction_id": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "deposit": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "last_triggered_at": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "last_updated": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "old_start_time": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "payout": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "production_and_venue_specs": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "refunded_in_credits": {
            "cast": "std::bool",
            "cardinality": "One",
            "readonly": False,
        },
        "reschedule_message": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "resolved_booking_dispute": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "seller_has_reviewed": {
            "cast": "std::bool",
            "cardinality": "One",
            "readonly": False,
        },
        "should_auto_publish": {
            "cast": "std::bool",
            "cardinality": "One",
            "readonly": False,
        },
        "week_out_notification_at": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "billing": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "week_out_notification": {
            "cast": "std::bool",
            "cardinality": "One",
            "readonly": False,
        },
        "capacity": {"cast": "std::int16", "cardinality": "One", "readonly": False},
        "has_extra_charge": {
            "cast": "std::bool",
            "cardinality": "One",
            "readonly": False,
        },
        "has_extra_payout": {
            "cast": "std::bool",
            "cardinality": "One",
            "readonly": False,
        },
    }


class Booking(Node[BookingInsert]):
    id: UUID = Field(..., allow_mutation=False)
    firebase_id: str = Field(..., allow_mutation=False)
    performance_length_mins: int = Field(..., allow_mutation=True)
    start_time: datetime = Field(..., allow_mutation=True)
    created_at: datetime = Field(..., allow_mutation=True)
    booking_flow: BookingFlow = Field(..., allow_mutation=True)
    location: str = Field(..., allow_mutation=True)
    negotiation_steps: str = Field(..., allow_mutation=True)
    status: BookingStatus = Field(..., allow_mutation=True)
    is_published: bool = Field(..., allow_mutation=True)
    indoors_or_outdoors: T.Optional[IndoorsOrOutdoors] = Field(
        None, allow_mutation=True
    )
    public_event_description: T.Optional[str] = Field(None, allow_mutation=True)
    admin_cancellation_message: T.Optional[str] = Field(None, allow_mutation=True)
    band_configuration: T.Optional[BandConfigurationOption] = Field(
        None, allow_mutation=True
    )
    booking_dispute: T.Optional[str] = Field(None, allow_mutation=True)
    buyer_has_reviewed: T.Optional[bool] = Field(None, allow_mutation=True)
    charge: T.Optional[str] = Field(None, allow_mutation=True)
    comments: T.Optional[str] = Field(None, allow_mutation=True)
    customer_balance_transaction_id: T.Optional[str] = Field(None, allow_mutation=True)
    deposit: T.Optional[str] = Field(None, allow_mutation=True)
    last_triggered_at: T.Optional[datetime] = Field(None, allow_mutation=True)
    last_updated: T.Optional[datetime] = Field(None, allow_mutation=True)
    old_start_time: T.Optional[datetime] = Field(None, allow_mutation=True)
    payout: T.Optional[str] = Field(None, allow_mutation=True)
    production_and_venue_specs: T.Optional[str] = Field(None, allow_mutation=True)
    refunded_in_credits: T.Optional[bool] = Field(None, allow_mutation=True)
    reschedule_message: T.Optional[str] = Field(None, allow_mutation=True)
    resolved_booking_dispute: T.Optional[str] = Field(None, allow_mutation=True)
    seller_has_reviewed: T.Optional[bool] = Field(None, allow_mutation=True)
    should_auto_publish: T.Optional[bool] = Field(None, allow_mutation=True)
    week_out_notification_at: T.Optional[datetime] = Field(None, allow_mutation=True)
    billing: T.Optional[Billing] = Field(None, allow_mutation=True)
    week_out_notification: T.Optional[bool] = Field(None, allow_mutation=True)
    capacity: T.Optional[int] = Field(None, allow_mutation=True)
    has_extra_charge: T.Optional[bool] = Field(None, allow_mutation=True)
    has_extra_payout: T.Optional[bool] = Field(None, allow_mutation=True)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": {"cast": "std::uuid", "cardinality": "One", "readonly": True},
        "firebase_id": {"cast": "std::str", "cardinality": "One", "readonly": True},
        "performance_length_mins": {
            "cast": "std::int16",
            "cardinality": "One",
            "readonly": False,
        },
        "start_time": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "created_at": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "booking_flow": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "location": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "negotiation_steps": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "status": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "is_published": {"cast": "std::bool", "cardinality": "One", "readonly": False},
        "indoors_or_outdoors": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "public_event_description": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "admin_cancellation_message": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "band_configuration": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "booking_dispute": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "buyer_has_reviewed": {
            "cast": "std::bool",
            "cardinality": "One",
            "readonly": False,
        },
        "charge": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "comments": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "customer_balance_transaction_id": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "deposit": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "last_triggered_at": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "last_updated": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "old_start_time": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "payout": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "production_and_venue_specs": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "refunded_in_credits": {
            "cast": "std::bool",
            "cardinality": "One",
            "readonly": False,
        },
        "reschedule_message": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "resolved_booking_dispute": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "seller_has_reviewed": {
            "cast": "std::bool",
            "cardinality": "One",
            "readonly": False,
        },
        "should_auto_publish": {
            "cast": "std::bool",
            "cardinality": "One",
            "readonly": False,
        },
        "week_out_notification_at": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "billing": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "week_out_notification": {
            "cast": "std::bool",
            "cardinality": "One",
            "readonly": False,
        },
        "capacity": {"cast": "std::int16", "cardinality": "One", "readonly": False},
        "has_extra_charge": {
            "cast": "std::bool",
            "cardinality": "One",
            "readonly": False,
        },
        "has_extra_payout": {
            "cast": "std::bool",
            "cardinality": "One",
            "readonly": False,
        },
    }
    _link_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "artist": {
            "cast": "Artist",
            "cardinality": "One",
            "readonly": False,
            "required": True,
        },
        "buyer": {
            "cast": "User",
            "cardinality": "One",
            "readonly": False,
            "required": True,
        },
        "account_exec": {
            "cast": "User",
            "cardinality": "One",
            "readonly": False,
            "required": False,
        },
        "venue": {
            "cast": "Venue",
            "cardinality": "One",
            "readonly": False,
            "required": False,
        },
    }

    async def artist(
        self,
        resolver: ArtistResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> Artist:
        return await self.resolve(
            edge_name="artist",
            edge_resolver=resolver or ArtistResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def buyer(
        self,
        resolver: UserResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> User:
        return await self.resolve(
            edge_name="buyer",
            edge_resolver=resolver or UserResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def account_exec(
        self,
        resolver: UserResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[User]:
        return await self.resolve(
            edge_name="account_exec",
            edge_resolver=resolver or UserResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def venue(
        self,
        resolver: VenueResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[Venue]:
        return await self.resolve(
            edge_name="venue",
            edge_resolver=resolver or VenueResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def update(
        self,
        given_resolver: BookingResolver = None,
        error_if_no_update: bool = False,
        batch: Batch = None,
        given_client: AsyncIOClient = None,
        artist: T.Optional[ArtistResolver] = None,
        buyer: T.Optional[UserResolver] = None,
        account_exec: T.Optional[UserResolver] = None,
        venue: T.Optional[VenueResolver] = None,
    ) -> None:
        set_links_d = {
            "artist": artist,
            "buyer": buyer,
            "account_exec": account_exec,
            "venue": venue,
        }
        set_links_d = {key: val for key, val in set_links_d.items() if val is not None}

        return await super().update(
            given_resolver=given_resolver,
            error_if_no_update=error_if_no_update,
            set_links_d=set_links_d,
            batch=batch,
            given_client=given_client,
        )

    class GraphORM:
        model_name = "Booking"
        client = client
        updatable_fields: T.Set[str] = {
            "account_exec",
            "admin_cancellation_message",
            "artist",
            "band_configuration",
            "billing",
            "booking_dispute",
            "booking_flow",
            "buyer",
            "buyer_has_reviewed",
            "capacity",
            "charge",
            "comments",
            "created_at",
            "customer_balance_transaction_id",
            "deposit",
            "has_extra_charge",
            "has_extra_payout",
            "indoors_or_outdoors",
            "is_published",
            "last_triggered_at",
            "last_updated",
            "location",
            "negotiation_steps",
            "old_start_time",
            "payout",
            "performance_length_mins",
            "production_and_venue_specs",
            "public_event_description",
            "refunded_in_credits",
            "reschedule_message",
            "resolved_booking_dispute",
            "seller_has_reviewed",
            "should_auto_publish",
            "start_time",
            "status",
            "venue",
            "week_out_notification",
            "week_out_notification_at",
        }
        exclusive_fields: T.Set[str] = {"firebase_id", "id"}


class BookingResolver(Resolver[Booking]):
    _node = Booking

    def artist(self, _: T.Optional[ArtistResolver] = None, /) -> BookingResolver:
        if "artist" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `artist` has already been provided."
            )
        self._nested_resolvers["artist"] = _ or ArtistResolver()
        return self

    def buyer(self, _: T.Optional[UserResolver] = None, /) -> BookingResolver:
        if "buyer" in self._nested_resolvers:
            raise ResolverException("A resolver for `buyer` has already been provided.")
        self._nested_resolvers["buyer"] = _ or UserResolver()
        return self

    def account_exec(self, _: T.Optional[UserResolver] = None, /) -> BookingResolver:
        if "account_exec" in self._nested_resolvers:
            raise ResolverException(
                "A resolver for `account_exec` has already been provided."
            )
        self._nested_resolvers["account_exec"] = _ or UserResolver()
        return self

    def venue(self, _: T.Optional[VenueResolver] = None, /) -> BookingResolver:
        if "venue" in self._nested_resolvers:
            raise ResolverException("A resolver for `venue` has already been provided.")
        self._nested_resolvers["venue"] = _ or VenueResolver()
        return self


Booking.GraphORM.resolver_type = BookingResolver


class ExternalBookingInsert(BaseModel):
    firebase_id: str
    performance_length_mins: int
    start_time: datetime
    is_published: bool
    indoors_or_outdoors: T.Optional[IndoorsOrOutdoors] = None
    public_event_description: T.Optional[str] = None
    artist_name: T.Optional[str] = None
    cover_image: T.Optional[str] = None
    last_triggered_at: T.Optional[datetime] = None
    venue: T.Optional[VenueResolver] = None

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "firebase_id": {"cast": "std::str", "cardinality": "One", "readonly": True},
        "performance_length_mins": {
            "cast": "std::int16",
            "cardinality": "One",
            "readonly": False,
        },
        "start_time": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "is_published": {"cast": "std::bool", "cardinality": "One", "readonly": False},
        "indoors_or_outdoors": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "public_event_description": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "artist_name": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "cover_image": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "last_triggered_at": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
    }


class ExternalBooking(Node[ExternalBookingInsert]):
    id: UUID = Field(..., allow_mutation=False)
    firebase_id: str = Field(..., allow_mutation=False)
    performance_length_mins: int = Field(..., allow_mutation=True)
    start_time: datetime = Field(..., allow_mutation=True)
    is_published: bool = Field(..., allow_mutation=True)
    indoors_or_outdoors: T.Optional[IndoorsOrOutdoors] = Field(
        None, allow_mutation=True
    )
    public_event_description: T.Optional[str] = Field(None, allow_mutation=True)
    artist_name: T.Optional[str] = Field(None, allow_mutation=True)
    cover_image: T.Optional[str] = Field(None, allow_mutation=True)
    last_triggered_at: T.Optional[datetime] = Field(None, allow_mutation=True)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": {"cast": "std::uuid", "cardinality": "One", "readonly": True},
        "firebase_id": {"cast": "std::str", "cardinality": "One", "readonly": True},
        "performance_length_mins": {
            "cast": "std::int16",
            "cardinality": "One",
            "readonly": False,
        },
        "start_time": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
        "is_published": {"cast": "std::bool", "cardinality": "One", "readonly": False},
        "indoors_or_outdoors": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "public_event_description": {
            "cast": "std::str",
            "cardinality": "One",
            "readonly": False,
        },
        "artist_name": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "cover_image": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "last_triggered_at": {
            "cast": "std::datetime",
            "cardinality": "One",
            "readonly": False,
        },
    }
    _link_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "venue": {
            "cast": "Venue",
            "cardinality": "One",
            "readonly": False,
            "required": False,
        }
    }

    async def venue(
        self,
        resolver: VenueResolver = None,
        refresh: bool = False,
        force_use_stale: bool = False,
    ) -> T.Optional[Venue]:
        return await self.resolve(
            edge_name="venue",
            edge_resolver=resolver or VenueResolver(),
            refresh=refresh,
            force_use_stale=force_use_stale,
        )

    async def update(
        self,
        given_resolver: ExternalBookingResolver = None,
        error_if_no_update: bool = False,
        batch: Batch = None,
        given_client: AsyncIOClient = None,
        venue: T.Optional[VenueResolver] = None,
    ) -> None:
        set_links_d = {"venue": venue}
        set_links_d = {key: val for key, val in set_links_d.items() if val is not None}

        return await super().update(
            given_resolver=given_resolver,
            error_if_no_update=error_if_no_update,
            set_links_d=set_links_d,
            batch=batch,
            given_client=given_client,
        )

    class GraphORM:
        model_name = "ExternalBooking"
        client = client
        updatable_fields: T.Set[str] = {
            "artist_name",
            "cover_image",
            "indoors_or_outdoors",
            "is_published",
            "last_triggered_at",
            "performance_length_mins",
            "public_event_description",
            "start_time",
            "venue",
        }
        exclusive_fields: T.Set[str] = {"firebase_id", "id"}


class ExternalBookingResolver(Resolver[ExternalBooking]):
    _node = ExternalBooking

    def venue(self, _: T.Optional[VenueResolver] = None, /) -> ExternalBookingResolver:
        if "venue" in self._nested_resolvers:
            raise ResolverException("A resolver for `venue` has already been provided.")
        self._nested_resolvers["venue"] = _ or VenueResolver()
        return self


ExternalBooking.GraphORM.resolver_type = ExternalBookingResolver


class DogInsert(BaseModel):
    slug: str
    name: T.Optional[str] = None

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "slug": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "name": {"cast": "std::str", "cardinality": "One", "readonly": False},
    }


class Dog(Node[DogInsert]):
    id: UUID = Field(..., allow_mutation=False)
    slug: str = Field(..., allow_mutation=True)
    name: T.Optional[str] = Field(None, allow_mutation=True)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {
        "id": {"cast": "std::uuid", "cardinality": "One", "readonly": True},
        "slug": {"cast": "std::str", "cardinality": "One", "readonly": False},
        "name": {"cast": "std::str", "cardinality": "One", "readonly": False},
    }
    _link_conversion_map: T.ClassVar[T.Dict[str, str]] = {}

    async def update(
        self,
        given_resolver: DogResolver = None,
        error_if_no_update: bool = False,
        batch: Batch = None,
        given_client: AsyncIOClient = None,
    ) -> None:
        set_links_d = {}
        set_links_d = {key: val for key, val in set_links_d.items() if val is not None}

        return await super().update(
            given_resolver=given_resolver,
            error_if_no_update=error_if_no_update,
            set_links_d=set_links_d,
            batch=batch,
            given_client=given_client,
        )

    class GraphORM:
        model_name = "Dog"
        client = client
        updatable_fields: T.Set[str] = {"name", "slug"}
        exclusive_fields: T.Set[str] = {"id", "slug"}


class DogResolver(Resolver[Dog]):
    _node = Dog


Dog.GraphORM.resolver_type = DogResolver

ArtistInsert.update_forward_refs()
UserInsert.update_forward_refs()
MovieInsert.update_forward_refs()
PersonInsert.update_forward_refs()
VenueInsert.update_forward_refs()
AnimalInsert.update_forward_refs()
FirebaseObjectInsert.update_forward_refs()
MetaBookingInsert.update_forward_refs()
BookingInsert.update_forward_refs()
ExternalBookingInsert.update_forward_refs()
DogInsert.update_forward_refs()
