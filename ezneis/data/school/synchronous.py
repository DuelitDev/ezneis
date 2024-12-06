# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from typing import Optional
from .common import *
from ...models import *
from ...wrappers.synchronous import SyncWrapper

__all__ = [
    "SyncSchoolData"
]


@dataclass()
class SyncSchoolData:
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

    def __init__(self, wrapper: SyncWrapper, *, info: SchoolInfo,
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

    def load_all(self, reload=False):
        self.load_schedules(reload)
        self.load_meals(reload)
        self.load_classrooms(reload)
        self.load_lecture_rooms(reload)
        self.load_timetable(reload)
        self.load_departments(reload)
        self.load_majors(reload)

    def load_schedules(self, reload=False):
        if self._schedules is not None and not reload:
            return
        self._schedules = SchedulesTuple(
            self._wrapper.get_schedules(self._code, self._region))

    def load_meals(self, reload=False):
        if self._meals is not None and not reload:
            return
        self._meals = MealsTuple(
            self._wrapper.get_meals(self._code, self._region))

    def load_classrooms(self, reload=False):
        if self._classrooms is not None and not reload:
            return
        self._classrooms = ClassroomsTuple(
            self._wrapper.get_classrooms(self._code, self._region))

    def load_lecture_rooms(self, reload=False):
        if self._lecture_rooms is not None and not reload:
            return
        self._lecture_rooms = LectureRoomsTuple(
            self._wrapper.get_lecture_rooms(self._code, self._region))

    def load_timetable(self, reload=False):
        if self._timetables is not None and not reload:
            return
        self._timetables = TimetablesTuple(
            self._wrapper.get_timetables(self._code, self._region))

    def load_departments(self, reload=False):
        if self._departments is not None and not reload:
            return
        self._departments = DepartmentsTuple(
            self._wrapper.get_departments(self._code, self._region))

    def load_majors(self, reload=False):
        if self._majors is not None and not reload:
            return
        self._majors = MajorsTuple(
            self._wrapper.get_majors(self._code, self._region))

    @property
    def info(self) -> SchoolInfo:
        return self._info

    @property
    def schedules(self) -> SchedulesTuple:
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

    @property
    def lecture_rooms(self) -> LectureRoomsTuple:
        if self._lecture_rooms is None:
            self.load_lecture_rooms()
        return self._lecture_rooms

    @property
    def timetables(self) -> TimetablesTuple:
        if self._timetables is None:
            self.load_timetable()
        return self._timetables

    @property
    def departments(self) -> DepartmentsTuple:
        if self._departments is None:
            self.load_departments()
        return self._departments

    @property
    def majors(self) -> MajorsTuple:
        if self._majors is None:
            self.load_majors()
        return self._majors
