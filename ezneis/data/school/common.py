# -*- coding: utf-8 -*-
from __future__ import annotations
from functools import cached_property
from ...models import (Schedule, Meal, Classroom, LectureRoom, Timetable,
                       Department, Major)

__all__ = [
    "SchedulesTuple",
    "MealsTuple",
    "ClassroomsTuple",
    "LectureRoomsTuple",
    "TimetablesTuple",
    "DepartmentsTuple",
    "MajorsTuple"
]


class SchedulesTuple(tuple[Schedule, ...]):
    pass


class MealsTuple(tuple[Meal, ...]):
    @cached_property
    def breakfasts(self) -> MealsTuple[Meal, ...]:
        return MealsTuple(i for i in self if i.time == i.time.BREAKFAST)

    @cached_property
    def lunches(self) -> MealsTuple[Meal, ...]:
        return MealsTuple(i for i in self if i.time == i.time.LUNCH)

    @cached_property
    def dinners(self) -> MealsTuple[Meal, ...]:
        return MealsTuple(i for i in self if i.time == i.time.DINNER)


class ClassroomsTuple(tuple[Classroom, ...]):
    @cached_property
    def grade0(self) -> ClassroomsTuple[Classroom, ...]:
        return ClassroomsTuple(i for i in self if i.grade == 0)

    @cached_property
    def grade1(self) -> ClassroomsTuple[Classroom, ...]:
        return ClassroomsTuple(i for i in self if i.grade == 1)

    @cached_property
    def grade2(self) -> ClassroomsTuple[Classroom, ...]:
        return ClassroomsTuple(i for i in self if i.grade == 2)

    @cached_property
    def grade3(self) -> ClassroomsTuple[Classroom, ...]:
        return ClassroomsTuple(i for i in self if i.grade == 3)

    @cached_property
    def grade4(self) -> ClassroomsTuple[Classroom, ...]:
        return ClassroomsTuple(i for i in self if i.grade == 4)

    @cached_property
    def grade5(self) -> ClassroomsTuple[Classroom, ...]:
        return ClassroomsTuple(i for i in self if i.grade == 5)

    @cached_property
    def grade6(self) -> ClassroomsTuple[Classroom, ...]:
        return ClassroomsTuple(i for i in self if i.grade == 6)

    @cached_property
    def grade7(self) -> ClassroomsTuple[Classroom, ...]:
        return ClassroomsTuple(i for i in self if i.grade == 7)


class LectureRoomsTuple(tuple[LectureRoom, ...]):
    @cached_property
    def grade0(self) -> LectureRoomsTuple[LectureRoom, ...]:
        return LectureRoomsTuple(i for i in self if i.grade == 0)

    @cached_property
    def grade1(self) -> LectureRoomsTuple[LectureRoom, ...]:
        return LectureRoomsTuple(i for i in self if i.grade == 1)

    @cached_property
    def grade2(self) -> LectureRoomsTuple[LectureRoom, ...]:
        return LectureRoomsTuple(i for i in self if i.grade == 2)

    @cached_property
    def grade3(self) -> LectureRoomsTuple[LectureRoom, ...]:
        return LectureRoomsTuple(i for i in self if i.grade == 3)

    @cached_property
    def grade4(self) -> LectureRoomsTuple[LectureRoom, ...]:
        return LectureRoomsTuple(i for i in self if i.grade == 4)

    @cached_property
    def grade5(self) -> LectureRoomsTuple[LectureRoom, ...]:
        return LectureRoomsTuple(i for i in self if i.grade == 5)

    @cached_property
    def grade6(self) -> LectureRoomsTuple[LectureRoom, ...]:
        return LectureRoomsTuple(i for i in self if i.grade == 6)

    @cached_property
    def grade7(self) -> LectureRoomsTuple[LectureRoom, ...]:
        return LectureRoomsTuple(i for i in self if i.grade == 7)

    @cached_property
    def spring_semester(self) -> LectureRoomsTuple[LectureRoom, ...]:
        return LectureRoomsTuple(i for i in self if i.semester == 1)

    @cached_property
    def fall_semester(self) -> LectureRoomsTuple[LectureRoom, ...]:
        return LectureRoomsTuple(i for i in self if i.semester == 2)


class TimetablesTuple(tuple[Timetable, ...]):
    pass


class DepartmentsTuple(tuple[Department, ...]):
    pass


class MajorsTuple(tuple[Major, ...]):
    pass
