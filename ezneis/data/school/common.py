# -*- coding: utf-8 -*-
from functools import cached_property
from ...models import Meal, Classroom

__all__ = [
    "MealsTuple",
    "ClassroomsTuple"
]


class MealsTuple(tuple[Meal, ...]):
    @cached_property
    def breakfasts(self) -> tuple[Meal, ...]:
        return tuple(i for i in self if i.time == i.time.BREAKFAST)

    @cached_property
    def lunches(self) -> tuple[Meal, ...]:
        return tuple(i for i in self if i.time == i.time.LUNCH)

    @cached_property
    def dinners(self) -> tuple[Meal, ...]:
        return tuple(i for i in self if i.time == i.time.DINNER)


class ClassroomsTuple(tuple[Classroom, ...]):
    @cached_property
    def grade0(self) -> tuple[Classroom, ...]:
        return tuple(i for i in self if i.grade == 0)

    @cached_property
    def grade1(self) -> tuple[Classroom, ...]:
        return tuple(i for i in self if i.grade == 1)

    @cached_property
    def grade2(self) -> tuple[Classroom, ...]:
        return tuple(i for i in self if i.grade == 2)

    @cached_property
    def grade3(self) -> tuple[Classroom, ...]:
        return tuple(i for i in self if i.grade == 3)

    @cached_property
    def grade4(self) -> tuple[Classroom, ...]:
        return tuple(i for i in self if i.grade == 4)

    @cached_property
    def grade5(self) -> tuple[Classroom, ...]:
        return tuple(i for i in self if i.grade == 5)

    @cached_property
    def grade6(self) -> tuple[Classroom, ...]:
        return tuple(i for i in self if i.grade == 6)

    @cached_property
    def grade7(self) -> tuple[Classroom, ...]:
        return tuple(i for i in self if i.grade == 7)
