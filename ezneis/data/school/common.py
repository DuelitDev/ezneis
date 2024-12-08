# -*- coding: utf-8 -*-
from __future__ import annotations
from datetime import datetime
from functools import cached_property
from ...models import (Schedule, Meal, Classroom, LectureRoom, Timetable,
                       Department, Major)
from ...utils.caches import lru_cache_instance

__all__ = [
    "SchedulesTuple",
    "MealsTuple",
    "ClassroomsTuple",
    "LectureRoomsTuple",
    "TimetablesTuple",
    "DepartmentsTuple",
    "MajorsTuple"
]

MAX_CACHE = 20


class SchedulesTuple(tuple[Schedule, ...]):
    @lru_cache_instance(maxsize=MAX_CACHE)
    def filter_by_year(self, year: int) -> SchedulesTuple:
        return SchedulesTuple(i for i in self if i.date.year == year)

    @lru_cache_instance(maxsize=MAX_CACHE)
    def filter_by_grade(self, grade: int) -> SchedulesTuple:
        if not 0 <= grade <= 7:
            raise ValueError("학년은 반드시 0 이상 7이하여야 합니다.")
        return SchedulesTuple(i for i in self if i.correspondence[grade])

    @cached_property
    def grade0(self) -> SchedulesTuple:
        return SchedulesTuple(i for i in self if i.correspondence.grade0)

    @cached_property
    def grade1(self) -> SchedulesTuple:
        return SchedulesTuple(i for i in self if i.correspondence.grade1)

    @cached_property
    def grade2(self) -> SchedulesTuple:
        return SchedulesTuple(i for i in self if i.correspondence.grade2)

    @cached_property
    def grade3(self) -> SchedulesTuple:
        return SchedulesTuple(i for i in self if i.correspondence.grade3)

    @cached_property
    def grade4(self) -> SchedulesTuple:
        return SchedulesTuple(i for i in self if i.correspondence.grade4)

    @cached_property
    def grade5(self) -> SchedulesTuple:
        return SchedulesTuple(i for i in self if i.correspondence.grade5)

    @cached_property
    def grade6(self) -> SchedulesTuple:
        return SchedulesTuple(i for i in self if i.correspondence.grade6)

    @cached_property
    def grade7(self) -> SchedulesTuple:
        return SchedulesTuple(i for i in self if i.correspondence.grade7)

    @lru_cache_instance(maxsize=MAX_CACHE)
    def filter_by_weekday(self, weekday: int) -> SchedulesTuple:
        return SchedulesTuple(i for i in self if i.date.weekday() == weekday)

    @cached_property
    def mondays(self) -> SchedulesTuple:
        return SchedulesTuple(i for i in self if i.date.weekday() == 0)

    @cached_property
    def tuesdays(self) -> SchedulesTuple:
        return SchedulesTuple(i for i in self if i.date.weekday() == 1)

    @cached_property
    def wednesdays(self) -> SchedulesTuple:
        return SchedulesTuple(i for i in self if i.date.weekday() == 2)

    @cached_property
    def thursdays(self) -> SchedulesTuple:
        return SchedulesTuple(i for i in self if i.date.weekday() == 3)

    @cached_property
    def fridays(self) -> SchedulesTuple:
        return SchedulesTuple(i for i in self if i.date.weekday() == 4)

    @cached_property
    def saturdays(self) -> SchedulesTuple:
        return SchedulesTuple(i for i in self if i.date.weekday() == 5)

    @cached_property
    def sundays(self) -> SchedulesTuple:
        return SchedulesTuple(i for i in self if i.date.weekday() == 6)

    @cached_property
    def today(self) -> SchedulesTuple:
        today = datetime.now().date()
        return SchedulesTuple(i for i in self if i.date == today)


class MealsTuple(tuple[Meal, ...]):
    @lru_cache_instance(maxsize=MAX_CACHE)
    def filter_by_year(self, year: int) -> MealsTuple:
        return MealsTuple(i for i in self if i.date.year == year)

    @lru_cache_instance(maxsize=MAX_CACHE)
    def filter_by_weekday(self, weekday: int) -> MealsTuple:
        return MealsTuple(i for i in self if i.date.weekday() == weekday)

    @cached_property
    def mondays(self) -> MealsTuple:
        return MealsTuple(i for i in self if i.date.weekday() == 0)

    @cached_property
    def tuesdays(self) -> MealsTuple:
        return MealsTuple(i for i in self if i.date.weekday() == 1)

    @cached_property
    def wednesdays(self) -> MealsTuple:
        return MealsTuple(i for i in self if i.date.weekday() == 2)

    @cached_property
    def thursdays(self) -> MealsTuple:
        return MealsTuple(i for i in self if i.date.weekday() == 3)

    @cached_property
    def fridays(self) -> MealsTuple:
        return MealsTuple(i for i in self if i.date.weekday() == 4)

    @cached_property
    def saturdays(self) -> MealsTuple:
        return MealsTuple(i for i in self if i.date.weekday() == 5)

    @cached_property
    def sundays(self) -> MealsTuple:
        return MealsTuple(i for i in self if i.date.weekday() == 6)

    @cached_property
    def today(self) -> MealsTuple:
        today = datetime.now().date()
        return MealsTuple(i for i in self if i.date == today)

    @cached_property
    def breakfasts(self) -> MealsTuple:
        return MealsTuple(i for i in self if i.time == i.time.BREAKFAST)

    @cached_property
    def lunches(self) -> MealsTuple:
        return MealsTuple(i for i in self if i.time == i.time.LUNCH)

    @cached_property
    def dinners(self) -> MealsTuple:
        return MealsTuple(i for i in self if i.time == i.time.DINNER)


class ClassroomsTuple(tuple[Classroom, ...]):
    @lru_cache_instance(maxsize=MAX_CACHE)
    def filter_by_year(self, year: int) -> ClassroomsTuple:
        return ClassroomsTuple(i for i in self if i.year == year)

    @lru_cache_instance(maxsize=MAX_CACHE)
    def filter_by_grade(self, grade: int) -> ClassroomsTuple:
        if not 0 <= grade <= 7:
            raise ValueError("학년은 반드시 0 이상 7이하여야 합니다.")
        return ClassroomsTuple(i for i in self if i.grade == grade)

    @cached_property
    def grade0(self) -> ClassroomsTuple:
        return ClassroomsTuple(i for i in self if i.grade == 0)

    @cached_property
    def grade1(self) -> ClassroomsTuple:
        return ClassroomsTuple(i for i in self if i.grade == 1)

    @cached_property
    def grade2(self) -> ClassroomsTuple:
        return ClassroomsTuple(i for i in self if i.grade == 2)

    @cached_property
    def grade3(self) -> ClassroomsTuple:
        return ClassroomsTuple(i for i in self if i.grade == 3)

    @cached_property
    def grade4(self) -> ClassroomsTuple:
        return ClassroomsTuple(i for i in self if i.grade == 4)

    @cached_property
    def grade5(self) -> ClassroomsTuple:
        return ClassroomsTuple(i for i in self if i.grade == 5)

    @cached_property
    def grade6(self) -> ClassroomsTuple:
        return ClassroomsTuple(i for i in self if i.grade == 6)

    @cached_property
    def grade7(self) -> ClassroomsTuple:
        return ClassroomsTuple(i for i in self if i.grade == 7)

    @lru_cache_instance(maxsize=MAX_CACHE)
    def filter_by_name(self, name: str | int) -> ClassroomsTuple:
        return ClassroomsTuple(i for i in self if i.name == str(name))


class LectureRoomsTuple(tuple[LectureRoom, ...]):
    @lru_cache_instance(maxsize=MAX_CACHE)
    def filter_by_year(self, year: int) -> LectureRoomsTuple:
        return LectureRoomsTuple(i for i in self if i.year == year)

    @lru_cache_instance(maxsize=MAX_CACHE)
    def filter_by_grade(self, grade: int) -> LectureRoomsTuple:
        if not 0 <= grade <= 7:
            raise ValueError("학년은 반드시 0 이상 7이하여야 합니다.")
        return LectureRoomsTuple(i for i in self if i.grade == grade)

    @cached_property
    def grade0(self) -> LectureRoomsTuple:
        return LectureRoomsTuple(i for i in self if i.grade == 0)

    @cached_property
    def grade1(self) -> LectureRoomsTuple:
        return LectureRoomsTuple(i for i in self if i.grade == 1)

    @cached_property
    def grade2(self) -> LectureRoomsTuple:
        return LectureRoomsTuple(i for i in self if i.grade == 2)

    @cached_property
    def grade3(self) -> LectureRoomsTuple:
        return LectureRoomsTuple(i for i in self if i.grade == 3)

    @cached_property
    def grade4(self) -> LectureRoomsTuple:
        return LectureRoomsTuple(i for i in self if i.grade == 4)

    @cached_property
    def grade5(self) -> LectureRoomsTuple:
        return LectureRoomsTuple(i for i in self if i.grade == 5)

    @cached_property
    def grade6(self) -> LectureRoomsTuple:
        return LectureRoomsTuple(i for i in self if i.grade == 6)

    @cached_property
    def grade7(self) -> LectureRoomsTuple:
        return LectureRoomsTuple(i for i in self if i.grade == 7)

    @lru_cache_instance(maxsize=MAX_CACHE)
    def filter_by_semester(self, semester: int) -> LectureRoomsTuple:
        return LectureRoomsTuple(i for i in self if i.semester == semester)

    @cached_property
    def spring_semester(self) -> LectureRoomsTuple:
        return LectureRoomsTuple(i for i in self if i.semester == 1)

    @cached_property
    def fall_semester(self) -> LectureRoomsTuple:
        return LectureRoomsTuple(i for i in self if i.semester == 2)

    @lru_cache_instance(maxsize=MAX_CACHE)
    def filter_by_name(self, name: str | int) -> LectureRoomsTuple:
        return LectureRoomsTuple(i for i in self if i.name == str(name))


class TimetablesTuple(tuple[Timetable, ...]):
    @lru_cache_instance(maxsize=MAX_CACHE)
    def filter_by_year(self, year: int) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.date.year == year)

    @lru_cache_instance(maxsize=MAX_CACHE)
    def filter_by_grade(self, grade: int) -> TimetablesTuple:
        if not 0 <= grade <= 7:
            raise ValueError("학년은 반드시 0 이상 7이하여야 합니다.")
        return TimetablesTuple(i for i in self if i.grade == grade)

    @cached_property
    def grade0(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.grade == 0)

    @cached_property
    def grade1(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.grade == 1)

    @cached_property
    def grade2(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.grade == 2)

    @cached_property
    def grade3(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.grade == 3)

    @cached_property
    def grade4(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.grade == 4)

    @cached_property
    def grade5(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.grade == 5)

    @cached_property
    def grade6(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.grade == 6)

    @cached_property
    def grade7(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.grade == 7)

    def filter_by_semester(self, semester: int) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.semester == semester)

    @cached_property
    def spring_semester(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.semester == 1)

    @cached_property
    def fall_semester(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.semester == 2)

    @lru_cache_instance(maxsize=MAX_CACHE)
    def filter_by_weekday(self, weekday: int) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.date.weekday() == weekday)

    @cached_property
    def mondays(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.date.weekday() == 0)

    @cached_property
    def tuesdays(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.date.weekday() == 1)

    @cached_property
    def wednesdays(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.date.weekday() == 2)

    @cached_property
    def thursdays(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.date.weekday() == 3)

    @cached_property
    def fridays(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.date.weekday() == 4)

    @cached_property
    def saturdays(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.date.weekday() == 5)

    @cached_property
    def sundays(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.date.weekday() == 6)

    @cached_property
    def today(self) -> TimetablesTuple:
        today = datetime.now().date()
        return TimetablesTuple(i for i in self if i.date == today)

    @lru_cache_instance(maxsize=MAX_CACHE)
    def filter_by_classroom_name(self, name: str | int) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.classroom_name == str(name))

    @lru_cache_instance(maxsize=MAX_CACHE)
    def filter_by_lecture_room_name(self, name: str | int) -> TimetablesTuple:
        return TimetablesTuple(
            i for i in self if i.lecture_room_name == str(name))

    @lru_cache_instance(maxsize=MAX_CACHE)
    def filter_by_period(self, period: int) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.period == period)

    @cached_property
    def period0(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.period == 0)

    @cached_property
    def period1(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.period == 1)

    @cached_property
    def period2(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.period == 2)

    @cached_property
    def period3(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.period == 3)

    @cached_property
    def period4(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.period == 4)

    @cached_property
    def period5(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.period == 5)

    @cached_property
    def period6(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.period == 6)

    @cached_property
    def period7(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.period == 7)

    @cached_property
    def period8(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.period == 8)

    @cached_property
    def period9(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.period == 9)

    @cached_property
    def period10(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.period == 10)

    @cached_property
    def period11(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.period == 11)

    @cached_property
    def period12(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.period == 12)

    @cached_property
    def period13(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.period == 13)

    @cached_property
    def period14(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.period == 14)

    @cached_property
    def period15(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.period == 15)

    @cached_property
    def period16(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.period == 16)

    @cached_property
    def period17(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.period == 17)

    @cached_property
    def period18(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.period == 18)

    @cached_property
    def period19(self) -> TimetablesTuple:
        return TimetablesTuple(i for i in self if i.period == 19)

class DepartmentsTuple(tuple[Department, ...]):
    pass


class MajorsTuple(tuple[Major, ...]):
    pass
