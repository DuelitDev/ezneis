# -*- coding: utf-8 -*-
from enum import Enum

__all__ = [
    "Region"
]


class Region(Enum):
    """
    The Region class is an enumeration of different regions in Korea.
    Each region is represented by a value that corresponds to a code.
    """
    # noqa = typo ignores for Jetbrains PyCharm IDE.
    UNSPECIFIED = "NAN"                                           # noqa
    """Represents an unspecified region with the value "NAN"."""  # noqa
    SEOUL       = "B10"                                           # noqa
    """Represents the Seoul region with the value "B10"."""       # noqa
    BUSAN       = "C10"                                           # noqa
    """Represents the Busan region with the value "C10"."""       # noqa
    DAEGU       = "D10"                                           # noqa
    """Represents the Daegu region with the value "D10"."""       # noqa
    INCHEON     = "E10"                                           # noqa
    """Represents the Incheon region with the value "E10"."""     # noqa
    GWANGJU     = "F10"                                           # noqa
    """Represents the Gwangju region with the value "F10"."""     # noqa
    DAEJEON     = "G10"                                           # noqa
    """Represents the Daejeon region with the value "G10"."""     # noqa
    ULSAN       = "H10"                                           # noqa
    """Represents the Ulsan region with the value "H10"."""       # noqa
    SEJONG      = "I10"                                           # noqa
    """Represents the Sejong region with the value "I10"."""      # noqa
    GYEONGGI    = "J10"                                           # noqa
    """Represents the Gyeonggi region with the value "J10"."""    # noqa
    GANGWON     = "K10"                                           # noqa
    """Represents the Gangwon region with the value "K10"."""     # noqa
    CHUNGBUK    = "M10"                                           # noqa
    """Represents the Chungbuk region with the value "M10"."""    # noqa
    CHUNGNAM    = "N10"                                           # noqa
    """Represents the Chungnam region with the value "N10"."""    # noqa
    JEONBUK     = "P10"                                           # noqa
    """Represents the Jeonnam region with the value "P10"."""     # noqa
    JEONNAM     = "Q10"                                           # noqa
    """Represents the Jeonnam region with the value "Q10"."""     # noqa
    GYEONGBUK   = "R10"                                           # noqa
    """Represents the Gyeonggi region with the value "R10"."""    # noqa
    GYEONGNAM   = "S10"                                           # noqa
    """Represents the Gyeonggnam region with the value "S10"."""  # noqa
    JEJU        = "T10"                                           # noqa
    """Represents the Jeju region with the value "T10"."""        # noqa
    FOREIGNER   = "V10"                                           # noqa
    """Represents the foreign region with the value "V10"."""     # noqa
