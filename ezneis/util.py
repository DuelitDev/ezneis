from datetime import date
from enum import Enum
from neispy import Neispy

__all__ = [
    "_get_sync_api",
    "_today_ymd_str",
    "_today_ym_str",
    "_today_y_str",
    "Region"
]

_USED_API = None


def _get_sync_api(*args, **kwargs):
    global _USED_API
    if not _USED_API:
        _USED_API = Neispy.sync(*args, **kwargs)
    return _USED_API


def _today_ymd_str() -> str:
    return date.today().strftime("%Y%m%d")


def _today_ym_str() -> str:
    return date.today().strftime("%Y%m")


def _today_y_str() -> str:
    return date.today().strftime("%Y")


class Region(Enum):
    """

    """
    UNSPECIFIED = "NAN"
    SEOUL       = "B10"
    BUSAN       = "C10"
    DAEGU       = "D10"
    INCHEON     = "E10"
    GWANGJU     = "F10"
    DAEJEON     = "G10"
    ULSAN       = "H10"
    SEJONG      = "I10"
    GYEONGGI    = "J10"
    GANGWON     = "K10"
    CHUNGBUK    = "M10"
    CHUNGNAM    = "N10"
    JEONBUK     = "P10"
    JEONNAM     = "Q10"
    GYEONGBUK   = "R10"
    GYEONGNAM   = "S10"
    JEJU        = "T10"
    FORIENGER   = "V10"
