# -*- coding: utf-8 -*-
from enum import Enum
from requests.compat import urljoin

__all__ = [
    "MAX_CACHE",
    "TIME_TO_LIVE",
    "Services",
    "urljoin",
]


MAX_CACHE = 64
TIME_TO_LIVE = 86400


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class Services(Enum):
    """
    나이스 교육정보 OPEN API 서비스 엔드포인트 열거형입니다.
    """
    SCHOOL_INFO   = "https://open.neis.go.kr/hub/schoolInfo"
    """학교 기본 정보입니다."""
    SCHEDULES     = "https://open.neis.go.kr/hub/SchoolSchedule"
    """학사일정입니다."""
    MEALS         = "https://open.neis.go.kr/hub/mealServiceDietInfo"
    """급식 식단 정보입니다."""
    CLASSROOMS    = "https://open.neis.go.kr/hub/classInfo"
    """학급 정보입니다."""
    LECTURE_ROOMS = "https://open.neis.go.kr/hub/tiClrminfo"
    """시간표 강의실 정보입니다."""
    TIMETABLE_E   = "https://open.neis.go.kr/hub/elsTimetable"
    """초등학교 시간표입니다."""
    TIMETABLE_M   = "https://open.neis.go.kr/hub/misTimetable"
    """중학교 시간표입니다."""
    TIMETABLE_H   = "https://open.neis.go.kr/hub/hisTimetable"
    """고등학교 시간표입니다."""
    TIMETABLE_S   = "https://open.neis.go.kr/hub/spsTimetable"
    """특수학교 시간표입니다."""
    DEPARTMENTS   = "https://open.neis.go.kr/hub/schulAflcoinfo"
    """학교 계열 정보입니다."""
    MAJOR         = "https://open.neis.go.kr/hub/schoolMajorInfo"
    """학교 학과 정보입니다."""
    ACADEMY_INFO  = "https://open.neis.go.kr/hub/acaInsTiInfo"
    """학원 교습소 정보입니다."""
