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


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class Services(Enum):
    """
    나이스 교육정보 OPEN API 서비스 엔드포인트 열거형입니다.
    """
    SCHOOL_INFO   = "schoolInfo"
    """학교 기본 정보입니다."""
    SCHEDULES     = "SchoolSchedule"
    """학사일정입니다."""
    MEALS         = "mealServiceDietInfo"
    """급식 식단 정보입니다."""
    CLASSROOMS    = "classInfo"
    """학급 정보입니다."""
    LECTURE_ROOMS = "tiClrminfo"
    """시간표 강의실 정보입니다."""
    TIMETABLES_E  = "elsTimetable"
    """초등학교 시간표입니다."""
    TIMETABLES_M  = "misTimetable"
    """중학교 시간표입니다."""
    TIMETABLES_H  = "hisTimetable"
    """고등학교 시간표입니다."""
    TIMETABLES_S  = "spsTimetable"
    """특수학교 시간표입니다."""
    DEPARTMENTS   = "schulAflcoinfo"
    """학교 계열 정보입니다."""
    MAJORS        = "schoolMajorinfo"
    """학교 학과 정보입니다."""
    ACADEMY_INFO  = "acaInsTiInfo"
    """학원 교습소 정보입니다."""
