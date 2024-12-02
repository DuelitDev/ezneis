# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from typing import Optional
from ..http.common import Services
from ..http.asynchronous import AsyncSession
from ..models import SchoolInfo, Schedule, Meal, Classroom
from ..parsers import (SchoolInfoParser, ScheduleParser, MealParser,
                       ClassroomParser)
from ..utils.region import Region

__all__ = [
    "AsyncWrapper"
]


class AsyncWrapper:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_school_info(self, code: str, region: Optional[Region] = None,
                              **kwargs) -> tuple[SchoolInfo, ...]:
        """
        Fetches the school info from school name asynchronously.

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
        data = await self._session.get(**params, **kwargs)
        return tuple(SchoolInfoParser.from_json(i) for i in data)

    async def get_schedules(self, code: str, region: Region,
                            date: Optional[str | tuple[str, str]] = None,
                            **kwargs) -> tuple[Schedule, ...]:
        if date is None:
            start_date = end_date = datetime.today().strftime("%Y%m")
        elif isinstance(date, str):
            start_date = end_date = date
        elif isinstance(date, tuple):
            start_date, end_date = date
        else:
            raise ValueError("date_query 인자가 유효하지 않습니다.")
        data = await self._session.get(
            Services.SCHEDULES,
            SD_SCHUL_CODE=code, ATPT_OFCDC_SC_CODE=region.value,
            AA_FROM_YMD=start_date, AA_TO_YMD=end_date, **kwargs
        )
        return tuple(ScheduleParser.from_json(i) for i in data)

    async def get_meals(self, code: str, region: Region,
                        date: Optional[str | tuple[str, str]] = None,
                        **kwargs) -> tuple[Meal, ...]:
        if date is None:
            today = datetime.today()
            temp = (today - timedelta(days=today.weekday()))
            end_date = (temp + timedelta(days=6)).strftime("%Y%m%d")
            start_date = temp.strftime("%Y%m%d")
        elif isinstance(date, str):
            start_date = end_date = date
        elif isinstance(date, tuple):
            start_date, end_date = date
        else:
            raise ValueError("date_query의 값이 유효하지 않습니다.")
        data = await self._session.get(
            Services.MEALS,
            SD_SCHUL_CODE=code, ATPT_OFCDC_SC_CODE=region.value,
            MLSV_FROM_YMD=start_date, MLSV_TO_YMD=end_date, **kwargs
        )
        return tuple(MealParser.from_json(i) for i in data)

    async def get_classrooms(self, code: str, region: Region,
                             year: Optional[int] = None, **kwargs
                             ) -> tuple[Classroom, ...]:
        if year is None:
            year = datetime.today().year
        data = await self._session.get(
            Services.CLASSROOMS,
            SD_SCHUL_CODE=code, ATPT_OFCDC_SC_CODE=region.value, AY=year,
            **kwargs
        )
        return tuple(ClassroomParser.from_json(i) for i in data)
