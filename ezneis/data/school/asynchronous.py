# -*- coding: utf-8 -*-
from asyncio import gather
from dataclasses import dataclass, field
from typing import Optional
from .common import *
from ...models import *
from ...wrappers.asynchronous import AsyncWrapper

__all__ = [
    "AsyncSchoolData"
]


@dataclass()
class AsyncSchoolData:
    _info: Optional[SchoolInfo] \
        = field(default=None, init=False)

    _schedules: Optional[SchedulesTuple] \
        = field(default=None, init=False)

    _meals: Optional[MealsTuple] \
        = field(default=None, init=False)

    _classrooms: Optional[ClassroomsTuple] \
        = field(default=None, init=False)

    _lecture_rooms: Optional[LectureRoomsTuple] \
        = field(default=None, init=False)

    _timetables: Optional[TimetablesTuple] \
        = field(default=None, init=False)

    _departments: Optional[DepartmentsTuple] \
        = field(default=None, init=False)

    _majors: Optional[MajorsTuple] \
        = field(default=None, init=False)

    def __init__(self, wrapper: AsyncWrapper, *, info: SchoolInfo,
                 schedules:     Optional[tuple[Schedule, ...]]    = None,
                 meals:         Optional[tuple[Meal, ...]]        = None,
                 classrooms:    Optional[tuple[Classroom, ...]]   = None,
                 lecture_rooms: Optional[tuple[LectureRoom, ...]] = None,
                 timetables:    Optional[tuple[Timetable, ...]]   = None,
                 departments:   Optional[tuple[Department, ...]]  = None,
                 majors:        Optional[tuple[Major, ...]]       = None):
        self._wrapper = wrapper
        self._code = info.code
        self._region = info.region
        self._info = info
        self._schedules = schedules
        self._meals = meals
        self._classrooms = classrooms
        self._lecture_rooms = lecture_rooms
        self._timetables = timetables
        self._departments = departments
        self._majors = majors

    async def load_all(self, reload=False):
        await gather(
            self.load_schedules(reload),
            self.load_meals(reload),
            self.load_classrooms(reload),
            self.load_lecture_rooms(reload),
            self.load_timetable(reload),
            self.load_departments(reload),
            self.load_majors(reload)
        )

    async def load_schedules(self, reload=False, *,
                             date: Optional[str | tuple[str, str]] = None,
                             **kwargs):
        if self._schedules is not None and not reload:
            return
        self._schedules = SchedulesTuple(await self._wrapper.get_schedules(
            **kwargs, code=self._code, region=self._region,
            date=date
        ))

    async def load_meals(self, reload=False, *,
                         date: Optional[str | tuple[str, str]] = None,
                         **kwargs):
        if self._meals is not None and not reload:
            return
        self._meals = MealsTuple(await self._wrapper.get_meals(
            **kwargs, code=self._code, region=self._region,
            date=date
        ))

    async def load_classrooms(self, reload=False, *,
                              year: Optional[int] = None,
                              grade: Optional[int] = None,
                              **kwargs):
        if self._classrooms is not None and not reload:
            return
        self._classrooms = ClassroomsTuple(await self._wrapper.get_classrooms(
            **kwargs, code=self._code, region=self._region,
            year=year, grade=grade,
        ))

    async def load_lecture_rooms(self, reload=False, *,
                                 year: Optional[int] = None,
                                 grade: Optional[int] = None,
                                 semester: Optional[int] = None,
                                 **kwargs):
        if self._lecture_rooms is not None and not reload:
            return
        self._lecture_rooms = LectureRoomsTuple(
            await self._wrapper.get_lecture_rooms(
                **kwargs, code=self._code, region=self._region,
                year=year, grade=grade, semester=semester
        ))

    async def load_timetable(self, reload=False, *,
                             date: Optional[str | tuple[str, str]] = None,
                             **kwargs):
        if self._timetables is not None and not reload:
            return
        self._timetables = TimetablesTuple(await self._wrapper.get_timetables(
            **kwargs, code=self._code, region=self._region,
            timetable_service=self._info.school_category.timetable_service,
            date=date
        ))

    async def load_departments(self, reload=False, **kwargs):
        if self._departments is not None and not reload:
            return
        self._departments = DepartmentsTuple(
            await self._wrapper.get_departments(
                **kwargs, code=self._code, region=self._region
        ))

    async def load_majors(self, reload=False, **kwargs):
        if self._majors is not None and not reload:
            return
        self._majors = MajorsTuple(await self._wrapper.get_majors(
            **kwargs, code=self._code, region=self._region
        ))

    @property
    async def info(self) -> SchoolInfo:
        return self._info

    @property
    async def schedules(self) -> SchedulesTuple:
        if self._schedules is None:
            await self.load_schedules()
        return self._schedules

    @property
    async def meals(self) -> MealsTuple:
        if self._meals is None:
            await self.load_meals()
        return self._meals

    @property
    async def classrooms(self) -> ClassroomsTuple:
        if self._classrooms is None:
            await self.load_classrooms()
        return self._classrooms

    @property
    async def lecture_rooms(self) -> LectureRoomsTuple:
        if self._lecture_rooms is None:
            await self.load_lecture_rooms()
        return self._lecture_rooms

    @property
    async def timetables(self) -> TimetablesTuple:
        if self._timetables is None:
            await self.load_timetable()
        return self._timetables

    @property
    async def departments(self) -> DepartmentsTuple:
        if self._departments is None:
            await self.load_departments()
        return self._departments

    @property
    async def majors(self) -> MajorsTuple:
        if self._majors is None:
            await self.load_majors()
        return self._majors
