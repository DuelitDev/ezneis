# -*- coding: utf-8 -*-
from enum import Enum
from requests.compat import urljoin

__all__ = [
    "BASE_URL",
    "MAX_CACHE",
    "TIME_TO_LIVE",
    "Services",
    "urljoin",
]


BASE_URL = "https://open.neis.go.kr/hub/"
MAX_CACHE = 64
TIME_TO_LIVE = 86400


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
