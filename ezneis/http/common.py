# -*- coding: utf-8 -*-
from enum import Enum
from requests.compat import urljoin

__all__ = [
    "BASE_URL",
    "Services",
    "urljoin",
]


BASE_URL = "https://open.neis.go.kr/hub/"


class Services(Enum):
    SCHOOL_INFO  = "schoolInfo"           # noqa
    SCHEDULE     = "SchoolSchedule"       # noqa
    MEAL         = "mealServiceDietInfo"  # noqa
    CLASSROOMS   = "classInfo"            # noqa
    TIMETABLE_E  = "elsTimetable"         # noqa
    TIMETABLE_M  = "misTimetable"         # noqa
    TIMETABLE_H  = "hisTimetable"         # noqa
    TIMETABLE_S  = "spsTimetable"         # noqa
    AFFILIATION  = "schoolAflcoInfo"      # noqa
    MAJOR        = "schoolMajorInfo"      # noqa
    ACADEMY_INFO = "acaInsTiInfo"         # noqa
