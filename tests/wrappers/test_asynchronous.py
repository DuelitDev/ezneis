import pytest
from tests import get_key
from asyncio import gather
from random import choice, randint, sample
from ezneis.http import AsyncSession, SyncSession
from ezneis.wrappers import AsyncWrapper, SyncWrapper
from ezneis.utils.region import Region


@pytest.fixture(scope="session", autouse=True)
def schools():
    samples = 10
    region = choice(list(Region))
    with SyncSession(get_key()) as session:
        wrapper = SyncWrapper(session)
        info = wrapper.get_school_info("", region, hint=150)
        if len(info) < samples:
            return info
        return sample(info, 10)


@pytest.mark.asyncio
async def test_get_school_info(schools):
    async with AsyncSession(get_key()) as session:
        wrapper = AsyncWrapper(session)
        results = await gather(*[
            wrapper.get_school_info(i.code, i.region)
            for i in schools
        ])
        cases = sum(map(len, results))
    print(f"\t\tTotal: {cases}")


@pytest.mark.asyncio
async def test_get_schedules(schools):
    async with AsyncSession(get_key()) as session:
        wrapper = AsyncWrapper(session)
        results = await gather(*[
            wrapper.get_schedules(i.code, i.region)
            for i in schools
        ])
        cases = sum(map(len, results))
    print(f"\t\tTotal: {cases}")


@pytest.mark.asyncio
async def test_get_meals(schools):
    async with AsyncSession(get_key()) as session:
        wrapper = AsyncWrapper(session)
        results = await gather(*[
            wrapper.get_meals(i.code, i.region)
            for i in schools
        ])
        cases = sum(map(len, results))
    print(f"\t\tTotal: {cases}")


@pytest.mark.asyncio
async def test_get_classrooms(schools):
    async with AsyncSession(get_key()) as session:
        wrapper = AsyncWrapper(session)
        results = await gather(*[
            wrapper.get_classrooms(i.code, i.region, grade=randint(1, 3))
            for i in schools
        ])
        cases = sum(map(len, results))
    print(f"\t\tTotal: {cases}")


@pytest.mark.asyncio
async def test_get_timetable(schools):
    async with AsyncSession(get_key()) as session:
        wrapper = AsyncWrapper(session)
        results = await gather(*[
            wrapper.get_timetable(
                i.code, i.region, i.school_category.get_timetable_service())
            for i in schools
        ])
        cases = sum(map(len, results))
    print(f"\t\tTotal: {cases}")


@pytest.mark.asyncio
async def test_get_majors(schools):
    async with AsyncSession(get_key()) as session:
        wrapper = AsyncWrapper(session)
        results = await gather(*[
            wrapper.get_majors(i.code, i.region)
            for i in schools
        ])
        cases = sum(map(len, results))
    print(f"\t\tTotal: {cases}")
