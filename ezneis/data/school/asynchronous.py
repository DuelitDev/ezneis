# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from typing import Optional
from .common import *
from ...exceptions import DataNotFoundException
from ...http.asynchronous import AsyncSession
from ...models import SchoolInfo
from ...wrappers.asynchronous import AsyncWrapper
from ...utils.async_property import AsyncProperty
from ...utils.region import Region

__all__ = [
    "AsyncSchoolData"
]


@dataclass()
class AsyncSchoolData:
    _info: Optional[SchoolInfo]\
        = field(default=None, init=False)

    _schedules: Optional[SchedulesTuple]\
        = field(default=None, init=False)

    _meals: Optional[MealsTuple]\
        = field(default=None, init=False)

    _classrooms: Optional[ClassroomsTuple]\
        = field(default=None, init=False)

    _lecture_rooms: Optional[LectureRoomsTuple]\
        = field(default=None, init=False)

    _timetables: Optional[TimetablesTuple]\
        = field(default=None, init=False)

    _departments: Optional[DepartmentsTuple]\
        = field(default=None, init=False)

    _majors: Optional[MajorsTuple]\
        = field(default=None, init=False)

    def __init__(self, ks: str | AsyncSession, *,
                 code: Optional[str] = None,
                 region: Optional[Region] = None,
                 info: Optional[SchoolInfo] = None):
        if code is None and info is None:
            raise ValueError("code 또는 info 인자는 반드시 전달해야 합니다.")
        if isinstance(ks, AsyncSession):
            self._wrapper = AsyncWrapper(ks)
        elif isinstance(ks, str):
            self._wrapper = AsyncWrapper(AsyncSession(ks))
        else:
            raise TypeError("ks 인자의 타입이 올바르지 않습니다.")
        self._code = code if info is None else info.code
        self._region = region if info is None else info.region
        self._info = info

    async def load_all(self, reload=False):
        await self.load_info(reload)
        await self.load_schedules(reload)
        await self.load_meals(reload)
        await self.load_classrooms(reload)

    async def load_info(self, reload=False):
        if self._info is not None and not reload:
            return
        temp = await self._wrapper.get_school_info(self._code, self._region)
        if not temp:
            raise DataNotFoundException
        info = temp[0]
        self._code = info.code
        self._region = info.region
        self._info = info

    async def load_schedules(self, reload=False):
        if self._schedules is not None and not reload:
            return
        self._schedules = SchedulesTuple(
            await self._wrapper.get_schedules(self._code, self._region))

    async def load_meals(self, reload=False):
        if self._meals is not None and not reload:
            return
        self._meals = MealsTuple(
            await self._wrapper.get_meals(self._code, self._region))

    async def load_classrooms(self, reload=False):
        if self._classrooms is not None and not reload:
            return
        self._classrooms = ClassroomsTuple(
            await self._wrapper.get_classrooms(self._code, self._region))

    async def load_lecture_rooms(self, reload=False):
        if self._lecture_rooms is not None and not reload:
            return
        self._lecture_rooms = LectureRoomsTuple(
            await self._wrapper.get_lecture_rooms(self._code, self._region))

    async def load_timetable(self, reload=False):
        if self._timetables is not None and not reload:
            return
        self._timetables = TimetablesTuple(
            await self._wrapper.get_timetables(self._code, self._region))

    async def load_departments(self, reload=False):
        if self._departments is not None and not reload:
            return
        self._departments = DepartmentsTuple(
            await self._wrapper.get_departments(self._code, self._region))

    async def load_majors(self, reload=False):
        if self._majors is not None and not reload:
            return
        self._majors = MajorsTuple(
            await self._wrapper.get_majors(self._code, self._region))

    @AsyncProperty
    async def info(self) -> SchoolInfo:
        if self._info is None:
            await self.load_info()
        return self._info

    @AsyncProperty
    async def schedules(self) -> SchedulesTuple:
        if self._schedules is None:
            await self.load_schedules()
        return self._schedules

    @AsyncProperty
    async def meals(self) -> MealsTuple:
        if self._meals is None:
            await self.load_meals()
        return self._meals

    @AsyncProperty
    async def classrooms(self) -> ClassroomsTuple:
        if self._classrooms is None:
            await self.load_classrooms()
        return self._classrooms

    @AsyncProperty
    async def lecture_rooms(self) -> LectureRoomsTuple:
        if self._lecture_rooms is None:
            await self.load_lecture_rooms()
        return self._lecture_rooms

    @AsyncProperty
    async def timetables(self) -> TimetablesTuple:
        if self._timetables is None:
            await self.load_timetable()
        return self._timetables

    @AsyncProperty
    async def departments(self) -> DepartmentsTuple:
        if self._departments is None:
            await self.load_departments()
        return self._departments

    @AsyncProperty
    async def majors(self) -> MajorsTuple:
        if self._majors is None:
            await self.load_majors()
        return self._majors
