# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from typing import Optional
from .common import MealsTuple, ClassroomsTuple
from ...http.asynchronous import AsyncSession
from ...models import SchoolInfo, SchoolSchedule
from ...wrappers.asynchronous import AsyncWrapper
from ...utils.async_property import AsyncProperty
from ...utils.region import Region

__all__ = [
    "AsyncSchoolData"
]


@dataclass()
class AsyncSchoolData:
    _info: Optional[SchoolInfo] = field(default=None, init=False)
    _schedules: Optional[tuple[SchoolSchedule, ...]]\
        = field(default=None, init=False)
    _meals: Optional[MealsTuple] = field(default=None, init=False)
    _classrooms: Optional[ClassroomsTuple] = field(default=None, init=False)

    def __init__(self, ks: str | AsyncSession, *,
                 code: Optional[str] = None,
                 region: Optional[Region] = None,
                 info: Optional[SchoolInfo] = None):
        if code is None and info is None:
            # TODO: Invalid Arguments.
            raise "Arg Error"
        if isinstance(ks, AsyncSession):
            self._wrapper = AsyncWrapper(ks)
        elif isinstance(ks, str):
            self._wrapper = AsyncWrapper(AsyncSession(ks))
        else:
            # TODO: Invalid Arguments.
            raise "Arg Error"
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
            # TODO: Data Not Found.
            raise "No Data."
        info = temp[0]
        self._code = info.code
        self._region = info.region
        self._info = info

    async def load_schedules(self, reload=False):
        if self._schedules is not None and not reload:
            return
        temp = await self._wrapper.get_schedules(self._code, self._region)
        if not temp:
            # TODO: Data Not Found.
            raise "No Data."
        self._schedules = temp

    async def load_meals(self, reload=False):
        if self._meals is not None and not reload:
            return
        temp = await self._wrapper.get_meals(self._code, self._region)
        if not temp:
            # TODO: Data Not Found.
            raise "No Data."
        self._meals = MealsTuple(temp)

    async def load_classrooms(self, reload=False):
        if self._classrooms is not None and not reload:
            return
        temp = await self._wrapper.get_classrooms(self._code, self._region)
        if not temp:
            # TODO: Data Not Found.
            raise "No Data."
        self._classrooms = ClassroomsTuple(temp)

    @AsyncProperty
    async def info(self) -> SchoolInfo:
        if self._info is None:
            await self.load_info()
        return self._info

    @AsyncProperty
    async def schedules(self) -> tuple[SchoolSchedule, ...]:
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
