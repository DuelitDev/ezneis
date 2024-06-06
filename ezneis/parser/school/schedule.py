from datetime import datetime
from ezneis.parser.core import *
from ezneis.types.school.schedule import *
from typing import Tuple

__all__ = [
    "SchoolScheduleParser"
]


class SchoolScheduleParser(Parser):
    """
    A parser class to extract schedule from provided data.
    """

    @classmethod
    def parse(cls, data) -> Tuple[SchoolSchedule, ...]:
        """
        Parse the schedule from the given data.

        :param data: The data to parse the schedule from.
        :return: The parsed schedule.
        """
        return tuple(cls._run_parsers(row) for row
                     in data.SchoolSchedule[1].row)

    @staticmethod
    def _parser1(r) -> SchoolSchedule:
        """
        :param r: The object containing schedule.
        :return: An instance of the `SchoolSchedule` class.
        """
        year = int(r.AY)
        part_time = (
            ScheduleTimeClassification.DAY   if r.DGHT_CRSE_SC_NM == "주간" else
            ScheduleTimeClassification.NIGHT if r.DGHT_CRSE_SC_NM == "야간" else
            ScheduleTimeClassification.NONE
        )
        event_name        = r.EVENT_NM
        event_description = r.EVENT_CNTNT
        event_corresponds = EventCorresponds(
            grade0=False,
            grade1=r.ONE_GRADE_EVENT_YN   == 'Y',
            grade2=r.TW_GRADE_EVENT_YN    == 'Y',
            grade3=r.THREE_GRADE_EVENT_YN == 'Y',
            grade4=r.FR_GRADE_EVENT_YN    == 'Y',
            grade5=r.FIV_GRADE_EVENT_YN   == 'Y',
            grade6=r.SIX_GRADE_EVENT_YN   == 'Y',
            grade7=False
        )
        event_type = (
            EventType.DAY_OFF if r.SBTR_DD_SC_NM == "휴업일" else
            EventType.HOLIDAY if r.SBTR_DD_SC_NM == "공휴일" else
            EventType.NONE
        )
        event_date = datetime.strptime(r.AA_YMD,   "%Y%m%d").date()
        return SchoolSchedule(
            year=year,
            time=part_time,
            name=event_name,
            description=event_description,
            corresponds=event_corresponds,
            type=event_type,
            date=event_date,
        )

    _parsers = (_parser1,)
