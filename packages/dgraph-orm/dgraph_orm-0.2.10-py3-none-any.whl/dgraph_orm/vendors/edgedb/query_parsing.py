# from dgraph_orm.resolver import get_fields_and_nested_fields
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from pydantic import BaseModel
import time
from dgraph_orm.vendors.edgedb import Node, Resolver, UpdateOperation, Batch
import uuid
from devtools import debug
import typing as T
import asyncio
from pydantic import EmailStr, conint
from enum import Enum
from dgraph_orm.vendors.edgedb.execute import query as execute_query
from fastapi.encoders import jsonable_encoder
import json
from pathlib import Path

from dgraph_orm.vendors.edgedb.gen import edgedb_DO as DB

# from dgraph_orm.vendors.edgedb.gen import aws as DB


async def test_query():
    # person = Person(name="jon", age=2, id=uuid.uuid4())
    # debug(person)
    user_resolver = DB.UserResolver()
    booking_resolver = DB.BookingResolver().limit(10).order_by("created_at desc")
    debug(user_resolver)
    users = await (
        user_resolver.filter(
            "(.name = <str>$name OR .slug = <str>$slug) AND .created_at < <datetime>$created_at",
            # ".slug = <str>$slug",
            variables={
                "slug": "fernandorojo1",
                "name": "Jeremy Berman",
                "created_at": datetime(
                    2021, 10, 15, 11, 25, tzinfo=ZoneInfo("America/New_York")
                ),
            },
        )
        # .offset(0)
        .order_by(".created_at desc")
        # .limit(1)
        .query()
    )
    debug(users)
    debug(user_resolver.dict())


async def test_get():
    # user = await UserResolver().gerror(slug="jeremyberman")
    user = (
        await DB.PersonResolver()
        # .filter(".name = <str>$name", variables={"name": "huan"})
        # .gerror(id="bb53a967-a161-11ec-9241-f78ab4083468")
        .gerror(slug="jeremy")
    )
    debug(user)

    try:
        user = await DB.UserResolver().gerror(
            not_exclusive="bb53a967-a161-11ec-9241-f78ab4083468"
        )
        debug(user)
    except Exception as e:
        print(e)


async def test_nested():
    booking_resolver = (
        DB.BookingResolver()
        .filter(
            ".created_at > <datetime>$created_at",
            variables={
                "created_at": datetime(2000, 10, 1, tzinfo=ZoneInfo("America/New_York"))
            },
        )
        .limit(10)
        .order_by(".start_time asc")
    )
    # print("DJD", booking_resolver.fields_including_nested_to_return)
    print("DJD", booking_resolver.to_str())

    print("HERE")
    user_resolver = (
        DB.UserResolver()
        .bookings(booking_resolver)
        .filter("exists .bookings and .name > <str>$name", variables={"name": "Juan"})
        # .filter("count(.bookings) > 0")
        .order_by("count(.bookings) desc")
    )
    # debug(user_resolver._query_variables)
    # print("USERRR ", user_resolver.fields_including_nested_to_return)
    print("HI THERE", user_resolver.to_str())
    debug(user_resolver._get_nested_query_variables())
    debug(DB.UserResolver._node)
    users = await user_resolver.limit(2).query()
    debug(users)


async def test_add():
    insert_person = DB.PersonInsert(
        first_name="Jon",
        last_name="Quack",
        tags={"hey", "yaaas"},
        ordered_tags=["coding", "python"],
        slug=random_str(10)
        # age=20,
        # created_at=datetime.now(tz=ZoneInfo("America/New_York")),
        # email=EmailStr("j@gmail.com"),
        # version=21,
    )
    p = await DB.Person.add(insert_person)
    debug(p)


async def raw_add_test():
    q_str = "WITH new_Person := (INSERT Person { slug := <str>$slug, first_name := <str>$first_name, last_name := <str>$last_name, tags := array_unpack(<array<str>>$tags) }) SELECT new_Person {first_name, last_name, tags}"
    variables = {
        "first_name": "J",
        "last_name": "M",
        "tags": list({"code", "python"}),
        "slug": random_str(10),
    }
    res = await execute_query(query_str=q_str, variables=variables, client=DB.client)
    debug(res)


async def test_raw_add_many():
    q_str = "WITH new_Persons := (WITH raw_data := <json>$data, FOR item in json_array_unpack(raw_data) UNION (INSERT Person {slug := <str>item['slug'], first_name := <str>item['first_name'], last_name := <str>item['last_name'], tags := array_unpack(<array<str>>item['tags']), created_at := <datetime>$created_at})) SELECT new_Persons {slug, id, first_name, last_name, tags, created_at}"
    variables = {
        "data": json.dumps(
            jsonable_encoder(
                [
                    {
                        "first_name": "J",
                        "slug": random_str(10),
                        "last_name": "Ber",
                        "tags": {"shee", "coding"},
                        "created_at": datetime.now(tz=ZoneInfo("America/New_York")),
                    },
                    {
                        "first_name": "R",
                        "slug": random_str(10),
                        "last_name": "Boo",
                        "tags": {"bloo"},
                    },
                ]
            )
        ),
        "created_at": datetime.now(tz=ZoneInfo("America/New_York")),
        # "created_at": None,
    }
    res = await execute_query(query_str=q_str, variables=variables, client=DB.client)
    debug(res)


async def test_raw_insert_without_for_loop():
    q_str = """
    WITH
        person_1 := (INSERT Person {first_name := <str>$first_name1, slug := <str>$slug1}),
        person_2 := (INSERT Person {first_name := <str>$first_name2, slug := <str>$slug2}),
        person_3 := (INSERT Person {first_name := <str>$first_name3, slug := <str>$slug3}),
        persons := (person_1 UNION person_2 UNION person_3)
    SELECT persons { id, first_name }
    """
    # q_str = "WITH new_Persons := (UNION ( INSERT Person {first_name := <str>$first_name1}, INSERT Person {first_name := <str>$first_name2} ) ), SELECT new_Persons {id, first_name}"
    variables = {
        "first_name1": "Reg",
        "first_name2": "Joe",
        "first_name3": "Juan",
        "slug1": random_str(10),
        "slug2": random_str(10),
        "slug3": random_str(10),
    }
    res = await execute_query(query_str=q_str, variables=variables, client=DB.client)
    debug(res)


async def test_add_many():
    persons = []
    for i in range(2):
        insert_person = DB.PersonInsert(
            first_name=f"Jon{i}",
            last_name=f"Quack{i}",
            tags={"hey", "yaaas"},
            ordered_tags=["coding", "python"],
            created_at=datetime.now(tz=ZoneInfo("America/New_York")),
            slug=random_str(10),
        )
        persons.append(insert_person)
    people = await DB.Person.add_many(inserts=persons)
    debug(people)


async def test_delete():
    insert_person = DB.PersonInsert(first_name="Juacko", slug=random_str(10))
    person = await DB.Person.add(insert_person)

    db_person = await DB.PersonResolver().gerror(id=person.id)
    await db_person.delete()
    assert await DB.PersonResolver().get(id=db_person.id) is None


async def test_delete_many():
    insert_persons = [
        DB.PersonInsert(first_name="Juacko", slug=random_str(10)),
        DB.PersonInsert(first_name="Juano", slug=random_str(10)),
    ]
    persons = await DB.Person.add_many(insert_persons)
    person_ids = [p.id for p in persons]
    db_persons = (
        await DB.PersonResolver()
        .filter(
            ".id in array_unpack(<array<uuid>>$ids)",
            variables={"ids": person_ids},
        )
        .query()
    )
    debug(db_persons)
    assert len(db_persons) == len(persons)
    await DB.Person.delete_many(db_persons)
    print("JUST DELETED THEM")
    debug(db_persons)
    new_db_persons = (
        await DB.PersonResolver()
        .filter(
            ".id in array_unpack(<array<uuid>>$ids)",
            variables={"ids": person_ids},
        )
        .query()
    )
    debug(new_db_persons)
    assert new_db_persons == []


async def test_update():
    person = (
        await DB.PersonResolver().limit(1).order_by("len(.first_name) asc").query()
    )[0]
    person.first_name = person.first_name + "hi"
    n = person.first_name
    await person.update()
    assert person.first_name == n
    db_person = await DB.PersonResolver().gerror(id=person.id)
    debug(db_person)
    assert db_person.first_name == n


async def test_update_many():
    """Actually just make a BATCH... but this can be later"""
    ...


async def test_link():
    jeremy = (
        await DB.PersonResolver()
        .filter(".first_name = <str>$first_name", {"first_name": "Jeremy"})
        .people_i_follow()
        .query()
    )[0]
    debug(jeremy)
    start = time.time()
    people = await jeremy.people_i_follow()
    took = time.time() - start
    assert took < 0.001
    start = time.time()
    people = await jeremy.people_i_follow(DB.PersonResolver().limit(100))
    took = time.time() - start
    assert took > 0.001
    print("LINK TESTING TOOK", took)
    debug(people)

    people = await jeremy.people_i_follow(DB.PersonResolver().my_followers())
    for p in people:
        s = time.time()
        followers = await p.my_followers()
        took = time.time() - s
        assert took < 0.001
        debug(followers)
        s = time.time()
        followers = await p.my_followers(resolver=DB.PersonResolver().people_i_follow())
        took = time.time() - s
        assert took > 0.001
        for follower in followers:
            ss = time.time()
            pp = await follower.people_i_follow()
            assert time.time() - ss
            debug(pp)


async def test_update_links():
    """will have to use detach -> figure out how to do this smartly"""
    jeremy = (
        await DB.PersonResolver()
        .filter(".first_name = <str>$first_name", {"first_name": "Jeremy"})
        .people_i_follow(DB.PersonResolver().limit(3).order_by(".created_at desc"))
        .my_followers()
        .best_friend()
        .query()
    )[0]
    # debug(jeremy)
    followings = await jeremy.people_i_follow(
        DB.PersonResolver().limit(3).order_by(".created_at desc")
    )
    followers = await jeremy.my_followers()
    debug(followings)
    # debug(followers)
    jeremy.tags.add("winkle")
    pr = (
        DB.PersonResolver()
        .filter(".first_name = <str>$first_name", {"first_name": "Fernando"})
        .limit(1)
        .update_operation(UpdateOperation.REPLACE)
    )
    debug(pr.all_filters_str())
    debug(pr._query_variables)
    jons = await (
        DB.PersonResolver()
        .filter(".first_name = <str>$first_name", {"first_name": "Jon"})
        .limit(5)
        .query()
    )
    await jeremy.update(
        best_friend=pr,
        people_i_follow=DB.Person.to_resolver_many(jons).update_operation(
            UpdateOperation.ADD
        ),
    )
    """
    await jeremy.update(
        set_links_d={
            "best_friend": ":= (SELECT DETACHED Person FILTER .first_name = <str>$first_name LIMIT 1)"
        },
        set_links_variables={"first_name": "Fernando"},
    )
    """
    debug(await jeremy.best_friend())
    debug(await jeremy.people_i_follow())
    # ideal

    """
    await jeremy.update(
        best_friend_replace=".first_name"
        # best friend add
        # best friend remove
    )
    """


async def test_batch():
    batch = Batch(print_status=True, client=DB.client)
    for i in range(100):
        insert_person = DB.PersonInsert(
            first_name=f"JonWHOO{i}",
            last_name=f"QuackERS{i}",
            tags={"hey", "yaaas"},
            slug=random_str(6),
        )
        p = await DB.Person.add(insert_person, batch=batch)
        assert p is None
    first_j = (
        await (
            DB.PersonResolver()
            .limit(1)
            .filter(".first_name = <str>$first_name", {"first_name": "J"})
            .query()
        )
    )[0]
    await first_j.delete(batch=batch)
    j_f_rez = DB.PersonResolver().filter(
        ".first_name in array_unpack(<array<str>>$first_names)",
        variables={"first_names": ["Jeremy", "Fernando"]},
    )

    jeremy_fernando = await j_f_rez.query()
    new_created_ats = []
    for person in jeremy_fernando:
        created_at = datetime.now(tz=ZoneInfo("America/New_York"))
        new_created_ats.append(created_at)
        person.created_at = created_at
        await person.update(batch=batch)
    debug(jeremy_fernando)
    ids = await batch.commit(chunk_size=10)
    debug(ids)
    jeremy_fernando_new = await j_f_rez.query()
    debug(new_created_ats)
    debug([p.created_at] for p in jeremy_fernando_new)
    assert [p.created_at for p in jeremy_fernando_new] == new_created_ats

    assert (await DB.PersonResolver().get(id=first_j.id)) == None


async def test_refresh():
    person = (await DB.PersonResolver().limit(1).query())[0]
    og_first_name = person.first_name
    person.first_name = "Sherbert " + og_first_name
    await person.refresh()
    assert person.first_name == og_first_name


async def test_transaction():
    from dgraph_orm.vendors.edgedb.gen.edgedb_DO import client

    async for tx in client.transaction():
        async with tx:

            first_j = (
                await (
                    DB.PersonResolver()
                    .limit(1)
                    .filter(".first_name = <str>$first_name", {"first_name": "J"})
                    .query(given_client=tx)
                )
            )[0]
            debug(first_j)
            for i in range(2):
                insert_person = DB.PersonInsert(
                    first_name=f"JonWHOO{i}",
                    last_name=f"QuackERS{i}",
                    tags={"hey", "yaaas"},
                    slug=random_str(6),
                )
                p = await DB.Person.add(insert_person, given_client=tx)
                debug(p)


from dgraph_orm.vendors.edgedb.constants import random_str, chunk_list, flatten_list


async def update_all_people():
    """NOT A TEST"""
    people = await DB.PersonResolver().query()
    batch = Batch(print_status=True, client=DB.client)
    for person in people:
        person.slug = f"{person.first_name}-{random_str(5)}"
        await person.update(batch=batch)
    res = await batch.commit(chunk_size=30)
    print(res)


async def test_upsert():
    # jeremy = await PersonResolver().gerror(slug="jeremy")
    # debug(jeremy)
    jeremy = await DB.Person.add(
        insert=DB.PersonInsert(
            first_name="Jeremy",
            slug="jeremy",
            last_name="Berman",
            tags={"Gru"},
            ordered_tags=["Skru"],
        ),
        # return_conflicting_model_on="slug",
        upsert_given_conflict_on="slug",
        # custom_on_conflict_str='UNLESS CONFLICT ON .slug ELSE (UPDATE Person SET {tags += "SPP0"})',
    )
    debug(jeremy)


from dgraph_orm.vendors.edgedb.introspection import (
    introspect_objects,
    introspect_scalars,
)


async def test_introspection():
    object_types = await introspect_objects(client=DB.client)
    debug(object_types)
    scalar_types = await introspect_scalars(client=DB.client)
    debug(scalar_types)


async def test_introspection_functions():
    object_types = await introspect_objects()
    for o in object_types:
        for p in [*o.properties, *o.links]:
            print(p.name, p.type_str)


async def test_generated():
    jeremy = await DB.PersonResolver().people_i_follow().gerror(slug="jeremy")
    debug(jeremy)
    for p in await jeremy.people_i_follow():
        debug(p)


async def test_generated_add():
    jonald_insert = DB.PersonInsert(
        first_name="Jonald",
        slug="jonald",
        tags={"wahoo"},
        best_friend=DB.PersonResolver()
        .filter(".slug = <std::str>$slugJ", {"slugJ": "jeremy"})
        .update_operation(UpdateOperation.REPLACE),
    )
    debug(jonald_insert)
    jonald = await DB.Person.add(
        jonald_insert,
        given_resolver=DB.PersonResolver().best_friend(),
        upsert_given_conflict_on="slug",
    )
    debug(jonald)
    debug(await jonald.best_friend())


async def test_generated_delete():
    jonald = await DB.PersonResolver().gerror(slug="jonald")
    await jonald.delete()


def people_inserts(n: int) -> T.List[DB.PersonInsert]:
    return [
        DB.PersonInsert(
            first_name=f"JonWHOO{i}",
            last_name=f"QuackERS{i}",
            tags={"hey", "yaaas"},
            slug=random_str(6),
            best_friend=DB.PersonResolver().filter(
                ".slug = <str>$slug", {"slug": "jeremy"}
            ),
        )
        for i in range(n)
    ]


async def add_lots_async() -> float:
    proms = [DB.Person.add(p) for p in people_inserts(n=500)]
    start = time.time()
    res = await asyncio.gather(*proms)
    took = (time.time() - start) * 1000
    debug(res)
    print("add lots async took", took, "ms")
    return took


async def add_lots_batch() -> float:
    batch = Batch(client=DB.client)
    [await DB.Person.add(p, batch=batch) for p in people_inserts(n=500)]
    start = time.time()
    await batch.commit(25)
    took = (time.time() - start) * 1000
    print("BATCH took", took, "ms")
    return took


async def test_extra_fields():
    class CalendarBookingType(str, Enum):
        external = "external"
        internal = "internal"

    class CalendarBooking(BaseModel):
        firebase_id: str
        artist_name: str
        # artist_profile_image: T.Optional[Image]
        # artist_cover_image: T.Optional[Image]
        start_time: datetime
        booking_type: CalendarBookingType

        # now for the click in fields
        artist_bio: T.Optional[str] = None
        public_event_description: T.Optional[str] = None
        performance_length_mins: int
        artist_slug: T.Optional[str] = None

    start = datetime.now(tz=ZoneInfo("America/New_York"))
    end = start + timedelta(days=90)
    meta_bookings = (
        await DB.MetaBookingResolver()
        .filter(
            ".is_published = <bool>$is_published AND .venue.slug = <str>$slug AND .start_time >= <datetime>$start AND .start_time <= <datetime>$end",
            {
                "start": start,
                "end": end,
                "slug": "beachcomberresort",
                "is_published": True,
            },
        )
        .order_by(".start_time asc")
        .limit(100)
        .offset(1)
        .extra_fields(
            "is_external := exists [is ExternalBooking].id, "
            "artist_name := [is ExternalBooking].artist_name ?? [is Booking].artist.name, "
            "artist_slug := [is Booking].artist.slug, "
            "cover_photo_external := [is ExternalBooking].cover_image, "
            "cover_image := [is Booking].artist.cover_image, artist_bio := [is Booking].artist.bio"
        )
        .query()
    )
    debug(meta_bookings)
    calendar_bookings: T.List[CalendarBooking] = []
    for meta in meta_bookings:
        calendar_bookings.append(
            CalendarBooking(
                firebase_id=meta.firebase_id,
                artist_name=meta.extra.get("artist_name"),
                start_time=meta.start_time,
                booking_type=CalendarBookingType.external
                if meta.extra.get("is_external")
                else CalendarBookingType.internal,
                artist_bio=meta.extra.get("artist_bio"),
                public_event_description=meta.public_event_description,
                performance_length_mins=meta.performance_length_mins,
                artist_slug=meta.extra.get("artist_slug"),
            )
        )
    debug(calendar_bookings)


async def test_bulk_reads():
    users = await DB.UserResolver().query()
    slugs = [u.slug for u in users]

    def create_proms(given_slugs):
        return [
            DB.UserResolver()
            .artists(DB.ArtistResolver().bookings(DB.BookingResolver().limit(10)))
            .venues(DB.VenueResolver().bookings(DB.BookingResolver().limit(10)))
            .gerror(slug=slug)
            for slug in given_slugs
        ]

    all_users_again = []
    start = time.time()
    for x in range(5):
        users_again = await asyncio.gather(*create_proms(slugs))
        all_users_again.extend(users_again)
    took = time.time() - start
    print(f"bulk reading {took=}")
    print(len(users_again))


async def investigate_bulk_load_bug():
    from dgraph_orm.vendors.edgedb.gen import local as db

    # db = DB

    batch = Batch(client=db.client)
    inserts = [
        db.PersonInsert(first_name="jay", slug=random_str(10)) for _ in range(50)
    ]
    print("starting")
    [await db.Person.add(insert=i, batch=batch) for i in inserts]
    res = await batch.commit()
    debug(res)


async def investigate_bulk_load_custom_code():
    import random
    import string

    def random_str(n: int) -> str:
        return "".join(random.choices(string.ascii_letters + string.digits, k=n))

    insert_strs: T.List[str] = []
    model_names: T.List[str] = []
    n = 50
    for i in range(n):
        model_name = f"model_{i}"
        insert_strs.append(
            f"{model_name}: (insert Person {{ first_name := <str>$first_name_{i}, slug := <str>$slug_{i} }} )"
        )

    union_str = f'models := ({" union ".join(model_names)})'
    insert_str = ",\n".join([*insert_strs, union_str])
    query_str = f"""
with
{insert_str}
select models {{id}}
    """
    first_name_variables = {f"first_name_{i}": random_str(10) for i in range(n)}
    variables = {}


async def using_for():
    n = 10
    query_s = f"""
with
    raw_data := <json>$data,
for item in json_array_unpack(raw_data) union (
    with
        # ordered_tags_var := <array<str>>item['ordered_tags'] if false else <array<str>>$empty_array,
        # ordered_tags := <OPTIONAL array<str>>json_get(item, 'ordered_tags_miss'),
        # ordered_tags := <array<str>>json_get(item, 'blo'),
        # ordered_tags := <array<str>>json_get(item, 'json_miss'),
        first_name_var := <str>item['first_name'] if exists <str>json_get(item, 'first_name') else <str>"notset",
        # last_name := <str>item['last_name'] ?? <str>"jon"
        last_name := <str>json_get(item, 'last_namer'),
        # best_friend_filter := <str>".first_name = <str>"Jeremy""
        # best_friend_filter := filter .slug in array_unpack(<array<str>>json_get(item, 'best_friend_slugs')),
        # filter_name := <str>".slug",
        best_friend := (select detached Person filter .slug = <str>json_get(item, 'best_friend', 'filter') limit <int16>json_get(item, 'best_friend', 'limit'))
    insert Person {{ first_name := first_name_var, slug := <str>item['slug'], last_name := last_name, best_friend := best_friend}} unless conflict on .slug else (update Person set {{ first_name := <str>item['first_name'] }})
) {{id, slug, last_name, ordered_tags, tags, inserted_at, created_at, best_friend: {{first_name}} }}
        """
    data = [
        {
            "first_name": random_str(10),
            "slug": random_str(10),
            # "slug": "EPwaYEelMB",
            # "last_name": "Scooby" if i % 2 == 0 else None,
            "last_name": None,
            "tags": ["hey"],
            # "tags": [],
            # "tags": [],
            "ordered_tags": ["spooky"],
            "best_friend_slugs": ["jeremy"],
            "best_friend": {"slug": "jeremy"},
            # "ordered_tags": None,
            # "ordered_tags": [],
        }
        for i in range(n)
    ]
    # learning -> if supposed to be a set or list or tuple but None, set to the empty versions of those things
    # this works if i can treat None as the same as an empty array or set or tuple
    # OK so NULL === {[], {}, ())... will just have to deal with this
    variables = {
        "data": json.dumps(data),
        # "empty_array": ["hi"],
    }
    res = await execute_query(client=DB.client, query_str=query_s, variables=variables)
    debug(res)


async def test_add_many_new():
    n = 10
    inserts = [DB.PersonInsert(first_name="jay", slug=random_str(10)) for _ in range(n)]
    res = await DB.Person.add_many(inserts=inserts, upsert_given_conflict_on="slug")
    debug(res)


from dgraph_orm.vendors.edgedb import creating_strings


async def creating_strings_testing():
    edge_filter_strs = [
        "best_friend := (select detached Person filter .slug = <str>json_get(item, 'best_friend', 'slug')"
    ]
    insert_str = creating_strings.insert_str_from_cls(
        insert_cls=DB.PersonInsert,
        node_cls=DB.Person,
        edge_filter_strs=edge_filter_strs,
        # upsert_given_conflict_on="slug",
        return_conflicting_model_on="slug",
    )
    # print(insert_str)
    insert = DB.PersonInsert(
        first_name="Juanald",
        slug="juanald",
        last_name=random_str(10),
        best_friend=DB.PersonResolver().filter(
            ".slug = <str>$slug", {"slug": "jeremy"}
        ),
    )
    people = await DB.Person.add_many(
        inserts=[insert],
        # upsert_given_conflict_on="slug",
        return_conflicting_model_on="slug",
    )
    debug(people)
    debug(await people[0].best_friend())


async def testing_with_dog():
    inserts = [
        DB.DogInsert(
            name=f"Spoof{i}wwz",
            # slug=random_str(10),
            slug=random_str(10) if i != 0 else "dog",
            # slug="dog",
        )
        for i in range(100)
    ]
    dogs = await DB.Dog.add_many(
        inserts=inserts,
        # return_conflicting_model_on="slug",
        upsert_given_conflict_on="slug",
    )
    debug(dogs)


async def testing_with_dog_raw():
    working_s = """
with
    raw_data := <json>$data,
for item in <tuple<slug: str, name: str>> json_array_unpack(raw_data) union (
    insert Dog {slug := item.slug, name := item.name}
    unless conflict on .slug else (select Dog)
) { slug, name, id }
    """
    testing_s = """
with
    raw_data := <json>$data,
for item in json_array_unpack(raw_data) union (
    with
        slug := <str>json_get(item, 'slug'),
        name := <str>json_get(item, 'name')
    insert Dog {slug := slug, name := name}
    # unless conflict on .slug else (select Dog)
    unless conflict on .slug else (update Dog set {slug := slug, name := name})
) { slug, name, id }
        """
    dogs = await execute_query(
        client=DB.client,
        query_str=testing_s,
        variables={
            "data": json.dumps(
                [
                    {"slug": "dog", "name": "jonny"},
                    {"slug": "dog00", "name": "jonnyald"},
                ]
            )
        },
    )
    debug(dogs)


async def testing_with_person():
    inserts = people_inserts(10_000)
    # people = await DB.Person.add_many(inserts=inerts)
    proms = []
    for chunk in chunk_list(inserts, chunk_size=10000):
        proms.append(
            DB.Person.add_many(
                chunk,
                edge_filter_strs=[
                    "best_friend := (select detached Person filter .slug = <str>json_get(item, 'best_friend', 'slug'))"
                    # "best_friend := (select detached Person order by .inserted_at asc limit 1)"
                ],
            )
        )
    res = flatten_list(await asyncio.gather(*proms))
    print(len(res))
    # print(len(people))
    if False:
        from dgraph_orm.vendors.edgedb.gen.edgedb_DO import client

        async for tx in client.transaction():
            async with tx:
                for insert in inerts:
                    p = await DB.Person.add(insert, given_client=tx)
                    debug(p)


async def testing_add_many_with_people():
    inserts = people_inserts(100)
    inserts[0].slug = "dog"
    inserts[1].slug = "dog"
    inserts[2].slug = "dog"
    # inserts[0].slug = "sjYZbHr"
    people = await DB.Person.add_many(
        inserts=inserts,
        # return_conflicting_model_on="slug",
        upsert_given_conflict_on="slug",
    )
    debug(people)


async def main():
    # await test_get()
    # await test_nested()
    # await test_add()
    # await raw_add_test()
    # await test_raw_add_many()
    # await test_raw_insert_without_for_loop()
    # await test_delete()
    # await test_update()
    # await test_link()
    # await test_update_links()
    # await test_batch()
    # await test_refresh()
    # await test_transaction()
    # await test_upsert()
    #
    # await test_generated_add()
    # await test_generated_delete()

    # await test_extra_fields()
    # await test_bulk_reads()
    # await investigate_bulk_load_bug()
    # await using_for()
    # await test_add_many_new()
    # await creating_strings_testing()
    # await testing_with_dog()
    # await testing_with_dog_raw()
    # await testing_with_person()
    await testing_add_many_with_people()

    # expensive ones
    # await add_lots_async()
    # await add_lots_batch()

    # buggy ones
    # await test_add_many()
    # await test_delete_many()

    # introspection ones
    # await test_introspection()
    # await test_introspection_functions()


if __name__ == "__main__":
    asyncio.run(main())
