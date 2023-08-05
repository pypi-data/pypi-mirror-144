import typing as T
import time
import orjson
from devtools import debug
import edgedb


async def query(
    client: edgedb.AsyncIOClient,
    query_str: str,
    variables: T.Optional[T.Dict[str, T.Any]] = None,
    only_one: bool = False,
    print_query: bool = True,
    print_variables: bool = False,
    print_raw_results: bool = False,
) -> T.Optional[dict]:
    """Returns a json str to be parsed by pydantic raw. Errors are raised by the lib!"""
    if not variables:
        variables = {}
    query_func = client.query_json if not only_one else client.query_single_json
    start = time.time()
    try:
        j_str = await query_func(query=query_str, **variables)
        j = orjson.loads(j_str)
        if print_raw_results:
            debug(j)
    except Exception as e:
        print(
            f"EdgeDB Query Exception: {e}, query_str and variables: {query_str=}, {variables=}"
        )
        raise e
    took_ms = (time.time() - start) * 1000
    print_s = ""
    if print_query:
        print_s += f" {query_str=} "
    if print_variables:
        print_s += f" {variables=} "
    if print_s:
        print_s = print_s.strip()
        print(print_s)
    print(f"took {took_ms}")
    return j
