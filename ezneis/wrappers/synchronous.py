# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Optional
from ..http.common import Services
from ..http.synchronous import SyncSession
from ..models import SchoolInfo, SchoolSchedule, Meal, Classroom
from ..parsers import (SchoolInfoParser, SchoolScheduleParser, MealParser,
                       ClassroomParser)
from ..utils.region import Region

__all__ = [
    "SyncWrapper"
]


class SyncWrapper:
    def __init__(self, session: SyncSession):
        self._session = session

    def get_school_info(self, code: str, region: Optional[Region] = None
                        ) -> tuple[SchoolInfo, ...]:
        """
        Fetches the school info from school name.

        :param code: School name or code.
        :param region: The region of the school.
        :return: Tuple of school info.
        """
        is_code = len(code) == 7 and (code.isdigit() or
                                      code[0] == "C" and code[1:].isdigit())
        params = {
            "service": Services.SCHOOL_INFO,
            "ATPT_OFCDC_SC_CODE": region.value if region is not None else "",
            "SD_SCHUL_CODE" if is_code else "SCHUL_NM": code,
        }
        data = self._session.get(**params)
        return tuple(SchoolInfoParser.from_json(i) for i in data)

    def get_schedules(self, code: str, region: Region,
                      date: Optional[str] = None) -> tuple[SchoolSchedule, ...]:
        if date is None:
            date = datetime.today().strftime("%Y%m")
        data = self._session.get(
            Services.SCHEDULE,
            SD_SCHUL_CODE=code, ATPT_OFCDC_SC_CODE=region.value, AA_YMD=date,
        )
        return tuple(SchoolScheduleParser.from_json(i) for i in data)

    def get_meals(self, code: str, region: Region,
                  date: Optional[str] = None) -> tuple[Meal, ...]:
        if date is None:
            date = datetime.today().strftime("%Y%m%d")
        data = self._session.get(
            Services.MEAL,
            SD_SCHUL_CODE=code, ATPT_OFCDC_SC_CODE=region.value, MLSV_YMD=date,
        )
        return tuple(MealParser.from_json(i) for i in data)

    def get_classrooms(self, code: str, region: Region,
                       year: Optional[int] = None) -> tuple[Classroom, ...]:
        if year is None:
            year = datetime.today().year
        data = self._session.get(
            Services.CLASSROOMS,
            SD_SCHUL_CODE=code, ATPT_OFCDC_SC_CODE=region.value, AY=year,
        )
        return tuple(ClassroomParser.from_json(i) for i in data)