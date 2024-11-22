# -*- coding: utf-8 -*-
from enum import Enum

__all__ = [
    "Timing",
    "Department",
]


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

    def __contains__(self, item) -> bool:
        """
        item이 이 주야 과정에 포함되는지 확인합니다.
        가령, `Timing.DAY in Timing.BOTH` 또는 `Timing.NIGHT in Timing.BOTH`는
        True를 반환합니다. 이와 달리, `Timing.BOTH in Timing.DAY`와
        `Timing.DAY in Timing.NIGHT`는 False를 반환합니다.

        :param item: 이 주야 과정과 비교할 항목입니다.
        :return: bool
        """
        if self is Timing.BOTH:
            return True
        return item == self


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class Department(Enum):
    """
    계열 유형을 나타내는 열거형입니다.
    """
    NORMAL        = "NORMAL"
    """일반계입니다."""
    VOCATIONAL    = "VOCATIONAL"
    """전문계입니다."""
    SPECIALIZED   = "SPECIALIZED"
    """특성화입니다."""
    INTERNATIONAL = "INTERNATIONAL"
    """국제계입니다."""
    BUSINESS      = "BUSINESS"
    """가사실업계입니다."""
    COMMERCE      = "COMMERCE"
    """상업계입니다."""
    TECHNICAL     = "TECHNICAL"
    """공업계입니다."""
    AGRICULTURE   = "AGRICULTURE"
    """농업계입니다."""
    FISHERIES     = "FISHERIES"
    """수산해양계입니다."""
    INTEGRATED    = "INTEGRATED"
    """통합계입니다."""
    LANGUAGE      = "LANGUAGE"
    """외국어계입니다."""
    SCIENCE       = "SCIENCE"
    """과학계입니다."""
    PHYSICAL      = "PHYSICAL"
    """체육계입니다."""
    ART           = "ART"
    """예술계입니다."""
    ALTERNATIVE   = "ALTERNATIVE"
    """대안입니다."""
    TRAINING      = "TRAINING"
    """공동실습소입니다."""