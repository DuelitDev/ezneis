from datetime import date
from enum import Enum

__all__ = [
    "_today_ymd_str",
    "_today_ym_str",
    "_today_y_str",
    "Region"
]


def _today_ymd_str() -> str:
    """
    Returns the current date in the format "YYYYMMDD".

    :return: The current date in the format "YYYYMMDD".
    """
    return date.today().strftime("%Y%m%d")


def _today_ym_str() -> str:
    """
    Get the current year and month as a string in the format 'YYYYMM'.

    :return: A string representing the current year and month
             in the format 'YYYYMM'.
    """
    return date.today().strftime("%Y%m")


def _today_y_str() -> str:
    """
    Get the current year as a formatted string.

    :return: The current year as a string in the format "YYYY".
    """
    return date.today().strftime("%Y")


class Region(Enum):
    """
    The Region class is an enumeration of different regions in Korea.
    Each region is represented by a value that corresponds to a code.
    """
    UNSPECIFIED = "NAN"
    """Represents an unspecified region with the value "NAN"."""
    SEOUL       = "B10"
    """Represents the Seoul region with the value "B10"."""
    BUSAN       = "C10"
    """Represents the Busan region with the value "C10"."""
    DAEGU       = "D10"
    """Represents the Daegu region with the value "D10"."""
    INCHEON     = "E10"
    """Represents the Incheon region with the value "E10"."""
    GWANGJU     = "F10"
    """Represents the Gwangju region with the value "F10"."""
    DAEJEON     = "G10"
    """Represents the Daejeon region with the value "G10"."""
    ULSAN       = "H10"
    """Represents the Ulsan region with the value "H10"."""
    SEJONG      = "I10"
    """Represents the Sejong region with the value "I10"."""
    GYEONGGI    = "J10"
    """Represents the Gyeonggi region with the value "J10"."""
    GANGWON     = "K10"
    """Represents the Gangwon region with the value "K10"."""
    CHUNGBUK    = "M10"
    """Represents the Chungbuk region with the value "M10"."""
    CHUNGNAM    = "N10"
    """Represents the Chungnam region with the value "N10"."""
    JEONBUK     = "P10"
    """Represents the Jeonnam region with the value "P10"."""
    JEONNAM     = "Q10"
    """Represents the Jeonnam region with the value "Q10"."""
    GYEONGBUK   = "R10"
    """Represents the Gyeonggi region with the value "R10"."""
    GYEONGNAM   = "S10"
    """Represents the Gyeonggnam region with the value "S10"."""
    JEJU        = "T10"
    """Represents the Jeju region with the value "T10"."""
    FOREIGNER   = "V10"
    """Represents the foreigner region with the value "V10"."""
