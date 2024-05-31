from datetime import date
from enum import Enum, auto
from ezneis.util import Region
from pydantic import BaseModel
from typing import Optional, Tuple

__all__ = [
    "Foundation",
    "SchoolType",
    "HighSchoolType",
    "HighSchoolDetailType",
    "Purpose",
    "SchoolPartTime",
    "EntrancePeriod",
    "StudentsSex",
    "SchoolInfo"
]


class Foundation(Enum):
    """

    """
    PUBLIC      = auto()
    PRIVATE     = auto()
    UNSPECIFIED = auto()


class SchoolType(Enum):
    """

    """
    ELEMENTARY     = auto()
    MIDDLE         = auto()
    HIGH           = auto()
    SECONDARY_MID  = auto()
    SECONDARY_HIGH = auto()
    MISC_ELE       = auto()
    MISC_MID       = auto()
    MISC_HIGH      = auto()
    SPECIAL        = auto()
    OTHERS         = auto()


class HighSchoolType(Enum):
    """

    """
    NORMAL     = auto()
    VOCATIONAL = auto()
    NONE       = auto()


class HighSchoolDetailType(Enum):
    """

    """
    NORMAL          = auto()
    SPECIALIZED     = auto()
    SPECIAL_PURPOSE = auto()
    AUTONOMOUS      = auto()
    OTHERS          = auto()
    NONE            = auto()


class Purpose(Enum):
    """

    """
    INTERNATIONAL = auto()
    PHYSICAL      = auto()
    ART           = auto()
    SCIENCE       = auto()
    LANGUAGE      = auto()
    INDUSTRY      = auto()
    NONE          = auto()


class SchoolPartTime(Enum):
    """

    """
    DAY         = auto()
    NIGHT       = auto()
    BOTH        = auto()


class EntrancePeriod(Enum):
    """

    """
    EARLY       = auto()
    LATER       = auto()
    BOTH        = auto()


class StudentsSex(Enum):
    """

    """
    MIXED       = auto()
    BOYS_ONLY   = auto()
    GIRLS_ONLY  = auto()


class SchoolInfo(BaseModel):
    """

    """
    code:              str
    name:              str
    english_name:      Optional[str]
    foundation:        Foundation
    types:             Tuple[SchoolType, HighSchoolType,
                             HighSchoolDetailType, Purpose]
    part_time:         SchoolPartTime
    entrance_period:   EntrancePeriod
    students_sex:      StudentsSex
    industry_supports: bool
    region:            Region
    address:           Optional[str]
    address_detail:    Optional[str]
    zip_code:          int
    jurisdiction_name: str
    tel_number:        str
    fax_number:        Optional[str]
    website:           Optional[str]
    found_date:        date
    anniversary:       date
