import pytest
import pytest_asyncio
from tests import get_key
from asyncio import gather
from random import randint
from ezneis.http import AsyncSession
from ezneis.wrappers import AsyncWrapper


@pytest_asyncio.fixture(scope="module")
async def wrapper():
    async with AsyncSession(get_key()) as session:
        yield AsyncWrapper(session)


@pytest.mark.asyncio
async def test_get_school_info(wrapper, region):
    results = await wrapper.get_school_info("", region, hint=150)
    print(f"\t\tTotal: {len(results)}")


@pytest.mark.asyncio
async def test_get_schedules(wrapper, schools):
    results = await gather(*[
        wrapper.get_schedules(i.code, i.region)
        for i in schools
    ])
    print(f"\t\tTotal: {sum(map(len, results))}")


@pytest.mark.asyncio
async def test_get_meals(wrapper, schools):
    results = await gather(*[
        wrapper.get_meals(i.code, i.region)
        for i in schools
    ])
    print(f"\t\tTotal: {sum(map(len, results))}")


@pytest.mark.asyncio
async def test_get_classrooms(wrapper, schools):
    results = await gather(*[
        wrapper.get_classrooms(i.code, i.region, grade=randint(1, 3))
        for i in schools
    ])
    print(f"\t\tTotal: {sum(map(len, results))}")


@pytest.mark.asyncio
async def test_get_timetable(wrapper, schools):
    results = await gather(*[
        wrapper.get_timetable(
            i.code, i.region, i.school_category.get_timetable_service())
        for i in schools
    ])
    print(f"\t\tTotal: {sum(map(len, results))}")


@pytest.mark.asyncio
async def test_get_majors(wrapper, schools):
    results = await gather(*[
        wrapper.get_majors(i.code, i.region)
        for i in schools
    ])
    print(f"\t\tTotal: {sum(map(len, results))}")
