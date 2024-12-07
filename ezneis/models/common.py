# -*- coding: utf-8 -*-
from enum import Enum
from typing import Optional
from ..http.common import Services

__all__ = [
    "CourseType",
    "SchoolCategory",
    "Timing"
]


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class CourseType(Enum):
    """
    학교 과정의 유형을 나타내는 열거형입니다.
    """
    PRESCHOOL  = "PRESCHOOL"
    """유치원 과정입니다."""
    ELEMENTARY = "ELEMENTARY"
    """초등학교 과정입니다."""
    MIDDLE     = "MIDDLE"
    """중학교 과정입니다."""
    HIGH       = "HIGH"
    """고등학교 과정입니다."""
    SPECIALITY = "SPECIALITY"
    """특수학교 과정입니다."""


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class SchoolCategory(Enum):
    """
    학교 종류를 나타내는 열거형입니다.
    """
    ELEMENTARY = "ELEMENTARY"
    """초등학교입니다."""
    MIDDLE     = "MIDDLE"
    """중학교입니다."""
    HIGH       = "HIGH"
    """고등학교입니다."""
    SEC_MID    = "SEC_MID"
    """방송 통신 중학교입니다."""
    SEC_HIGH   = "SEC_HIGH"
    """방송 통신 고등학교입니다."""
    MISC_ELE   = "MISC_ELE"
    """초등학교 과정 각종 학교입니다."""
    MISC_MID   = "MISC_MID"
    """중학교 과정 각종 학교입니다."""
    MISC_HIGH  = "MISC_HIGH"
    """고등학교 과정 각종 학교입니다."""
    SPECIAL    = "SPECIAL"
    """특수 학교입니다."""
    OTHERS     = "OTHERS"
    """기타 종류의 학교입니다."""

    @property
    def timetable_service(self) -> Optional[Services]:
        """
        열거형이 속하는 시간표 서비스 열거형을 반환합니다.
        가령, `HIGH`, `SEC_HIGH`, `MISC_HIGH`는 `Services.TIMETABLE_H`를
        반환합니다.

        :return: Services
        """
        match self:
            case (SchoolCategory.HIGH | SchoolCategory.SEC_HIGH |
                  SchoolCategory.MISC_HIGH):
                return Services.TIMETABLES_H
            case (SchoolCategory.MIDDLE | SchoolCategory.SEC_MID |
                  SchoolCategory.MISC_MID):
                return Services.TIMETABLES_M
            case SchoolCategory.ELEMENTARY | SchoolCategory.MISC_ELE:
                return Services.TIMETABLES_E
            case SchoolCategory.SPECIAL:
                return Services.TIMETABLES_S
            case _:
                return None


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class Timing(Enum):
    """
    주야 과정을 나타내는 열거형입니다.
    """
    DAY   = "DAY"
    """주간 과정입니다."""
    NIGHT = "NIGHT"
    """야간 과정입니다."""
    BOTH  = "BOTH"
    """주간과 야간을 모두 포함하는 과정입니다."""
    INDUSTRY_SPECIAL = "INDUSTRY_SPECIAL"
    """산업체 특별 과정입니다."""

    def __contains__(self, item) -> bool:
        """
        item이 이 주야 과정에 포함되는지 확인합니다.
        가령, `Timing.DAY in Timing.BOTH` 또는 `Timing.NIGHT in Timing.BOTH`는
        True를 반환합니다. 이와 달리, `Timing.BOTH in Timing.DAY`와
        `Timing.DAY in Timing.NIGHT`는 False를 반환합니다.

        :param item: 이 주야 과정과 비교할 항목입니다.
        :return: bool
        """
        if self == Timing.BOTH and item != Timing.INDUSTRY_SPECIAL:
            return True
        return item == self
