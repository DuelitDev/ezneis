import pytest
from tests import get_key
from random import randint
from ezneis.http import SyncSession
from ezneis.wrappers import SyncWrapper


@pytest.fixture(scope="module")
def wrapper():
    with SyncSession(get_key()) as session:
        yield SyncWrapper(session)


def test_get_school_info(wrapper, region):
    result = wrapper.get_school_info("", region, hint=150)
    print(f"\t\tTotal: {len(result)}")


def test_get_schedules(wrapper, schools):
    cases = 0
    for i in schools:
        result = wrapper.get_schedules(i.code, i.region)
        cases += len(result)
    print(f"\t\tTotal: {cases}")


def test_get_meals(wrapper, schools):
    cases = 0
    for i in schools:
        result = wrapper.get_meals(i.code, i.region)
        cases += len(result)
    print(f"\t\tTotal: {cases}")


def test_get_classrooms(wrapper, schools):
    cases = 0
    for i in schools:
        result = wrapper.get_classrooms(i.code, i.region, grade=randint(1, 3))
        cases += len(result)
    print(f"\t\tTotal: {cases}")


def test_get_timetable(wrapper, schools):
    cases = 0
    for i in schools:
        result = wrapper.get_timetable(
            i.code, i.region, i.school_category.get_timetable_service())
        cases += len(result)
    print(f"\t\tTotal: {cases}")


def test_get_majors(wrapper, schools):
    cases = 0
    for i in schools:
        result = wrapper.get_majors(i.code, i.region)
        cases += len(result)
    print(f"\t\tTotal: {cases}")
