import pytest
from tests import get_key
from random import choice, randint, sample
from ezneis.http import SyncSession
from ezneis.wrappers import SyncWrapper
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


def test_get_school_info(schools):
    cases = 0
    with SyncSession(get_key()) as session:
        wrapper = SyncWrapper(session)
        for i in schools:
            result = wrapper.get_school_info(i.code, i.region)
            cases += len(result)
    print(f"\t\tTotal: {cases}")


def test_get_schedules(schools):
    cases = 0
    with SyncSession(get_key()) as session:
        wrapper = SyncWrapper(session)
        for i in schools:
            result = wrapper.get_schedules(i.code, i.region)
            cases += len(result)
    print(f"\t\tTotal: {cases}")


def test_get_meals(schools):
    cases = 0
    with SyncSession(get_key()) as session:
        wrapper = SyncWrapper(session)
        for i in schools:
            result = wrapper.get_meals(i.code, i.region)
            cases += len(result)
    print(f"\t\tTotal: {cases}")


def test_get_classrooms(schools):
    cases = 0
    with SyncSession(get_key()) as session:
        wrapper = SyncWrapper(session)
        for i in schools:
            result = wrapper.get_classrooms(
                i.code, i.region, grade=randint(1, 3))
            cases += len(result)
    print(f"\t\tTotal: {cases}")


def test_get_timetable(schools):
    cases = 0
    with SyncSession(get_key()) as session:
        wrapper = SyncWrapper(session)
        for i in schools:
            result = wrapper.get_timetable(
                i.code, i.region, i.school_category.get_timetable_service())
            cases += len(result)
    print(f"\t\tTotal: {cases}")


def test_get_majors(schools):
    cases = 0
    with SyncSession(get_key()) as session:
        wrapper = SyncWrapper(session)
        for i in schools:
            result = wrapper.get_majors(i.code, i.region)
            cases += len(result)
    print(f"\t\tTotal: {cases}")
