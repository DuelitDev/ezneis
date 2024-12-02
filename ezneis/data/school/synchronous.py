# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from typing import Optional
from .common import MealsTuple, ClassroomsTuple
from ...exceptions import DataNotFoundException
from ...http.synchronous import SyncSession
from ...models import SchoolInfo, SchoolSchedule, Major
from ...wrappers.synchronous import SyncWrapper
from ...utils.region import Region

__all__ = [
    "SyncSchoolData"
]


@dataclass()
class SyncSchoolData:
    _info: Optional[SchoolInfo] = field(default=None, init=False)
    _schedules: Optional[tuple[SchoolSchedule, ...]]\
        = field(default=None, init=False)
    _meals: Optional[MealsTuple] = field(default=None, init=False)
    _classrooms: Optional[ClassroomsTuple] = field(default=None, init=False)
    _majors: Optional[tuple[Major, ...]] = field(default=None, init=False)

    def __init__(self, ks: str | SyncSession, *,
                 code: Optional[str] = None,
                 region: Optional[Region] = None,
                 info: Optional[SchoolInfo] = None):
        if code is None and info is None:
            raise ValueError("code 또는 info 인자는 반드시 전달해야 합니다.")
        if isinstance(ks, SyncSession):
            self._wrapper = SyncWrapper(ks)
        elif isinstance(ks, str):
            self._wrapper = SyncWrapper(SyncSession(ks))
        else:
            raise TypeError("ks 인자의 타입이 올바르지 않습니다.")
        self._code = code if info is None else info.code
        self._region = region if info is None else info.region
        self._info = info

    def load_all(self, reload=False):
        self.load_info(reload)
        self.load_schedules(reload)
        self.load_meals(reload)
        self.load_classrooms(reload)

    def load_info(self, reload=False):
        if self._info is not None and not reload:
            return
        temp = self._wrapper.get_school_info(self._code, self._region)
        if not temp:
            raise DataNotFoundException
        info = temp[0]
        self._code = info.code
        self._region = info.region
        self._info = info

    def load_schedules(self, reload=False):
        if self._schedules is not None and not reload:
            return
        self._schedules = self._wrapper.get_schedules(self._code, self._region)

    def load_meals(self, reload=False):
        if self._meals is not None and not reload:
            return
        self._meals = MealsTuple(self._wrapper.get_meals(
            self._code, self._region))

    def load_classrooms(self, reload=False):
        if self._classrooms is not None and not reload:
            return
        self._classrooms = ClassroomsTuple(self._wrapper.get_classrooms(
            self._code, self._region))

    @property
    def info(self) -> SchoolInfo:
        if self._info is None:
            self.load_info()
        return self._info

    @property
    def schedules(self) -> tuple[SchoolSchedule, ...]:
        if self._schedules is None:
            self.load_schedules()
        return self._schedules

    @property
    def meals(self) -> MealsTuple:
        if self._meals is None:
            self.load_meals()
        return self._meals

    @property
    def classrooms(self) -> ClassroomsTuple:
        if self._classrooms is None:
            self.load_classrooms()
        return self._classrooms
