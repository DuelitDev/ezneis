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
    "SchoolTimeClassification",
    "EntrancePeriod",
    "StudentsSex",
    "SchoolInfo"
]


class Foundation(Enum):
    """
    Enumeration representing the type of foundation of a school.
    """
    PUBLIC      = auto()
    """Represents a public school."""
    PRIVATE     = auto()
    """Represents a private school."""
    UNSPECIFIED = auto()
    """Represents an unspecified type of school foundation."""


class SchoolType(Enum):
    """
    Enumeration representing the type of school.
    """
    ELEMENTARY     = auto()
    """Represents an elementary school."""
    MIDDLE         = auto()
    """Represents a middle school."""
    HIGH           = auto()
    """Represents a high school."""
    SECONDARY_MID  = auto()
    """Represents an open secondary middle school."""
    SECONDARY_HIGH = auto()
    """Represents an open secondary high school."""
    MISC_ELE       = auto()
    """Represents a miscellaneous elementary school."""
    MISC_MID       = auto()
    """Represents a miscellaneous middle school."""
    MISC_HIGH      = auto()
    """Represents a miscellaneous high school."""
    SPECIAL        = auto()
    """Represents a special school."""
    OTHERS         = auto()
    """Represents other types of schools not listed."""


class HighSchoolType(Enum):
    """
    Enumeration representing the type of high school.
    """
    NORMAL     = auto()
    """Represents a normal high school."""
    VOCATIONAL = auto()
    """Represents a vocational high school."""
    NONE       = auto()
    """Represents no specific type of high school."""


class HighSchoolDetailType(Enum):
    """
    Enumeration representing detailed types of high schools.
    """
    NORMAL          = auto()
    """Represents a normal high school."""
    SPECIALIZED     = auto()
    """Represents a specialized high school."""
    SPECIAL_PURPOSE = auto()
    """Represents a special purpose high school."""
    AUTONOMOUS      = auto()
    """Represents an autonomous high school."""
    OTHERS          = auto()
    """Represents other types of high schools not listed."""
    NONE            = auto()
    """Represents no specific detail type of high school."""


class Purpose(Enum):
    """
    Enumeration representing the primary purpose of a school.
    """
    INTERNATIONAL = auto()
    """Represents a school with an international focus."""
    PHYSICAL      = auto()
    """Represents a school with a focus on physical education."""
    ART           = auto()
    """Represents a school with an art focus."""
    SCIENCE       = auto()
    """Represents a school with a science focus."""
    LANGUAGE      = auto()
    """Represents a school with a language focus."""
    INDUSTRY      = auto()
    """Represents a school with an industry focus."""
    NONE          = auto()
    """Represents a school with no specific purpose."""


class SchoolTimeClassification(Enum):
    """
    Enumeration for classifying school operational times.
    """
    DAY         = auto()
    """Represents a school that operates during the daytime."""
    NIGHT       = auto()
    """Represents a school that operates during the nighttime."""
    BOTH        = auto()
    """Represents a school that operates during both daytime and nighttime."""


class EntrancePeriod(Enum):
    """
    Enumeration representing the entrance period of a school.
    """
    EARLY       = auto()
    """Represents an early entrance period."""
    LATER       = auto()
    """Represents a later entrance period."""
    BOTH        = auto()
    """Represents both early and later entrance periods."""


class StudentsSex(Enum):
    """
    Enumeration representing the gender composition of a school's student body.
    """
    MIXED       = auto()
    """Represents a mixed-gender school."""
    BOYS_ONLY   = auto()
    """Represents a boys-only school."""
    GIRLS_ONLY  = auto()
    """Represents a girls-only school."""


class SchoolInfo(BaseModel):
    """
    Model representing detailed information about a school.
    """
    code:              str
    """The unique code of the school."""
    name:              str
    """The name of the school."""
    english_name:      Optional[str]
    """The English name of the school."""
    foundation:        Foundation
    """The foundation type of the school."""
    types:             Tuple[SchoolType, HighSchoolType,
                             HighSchoolDetailType, Purpose]
    """The types and purpose of the school."""
    time:              SchoolTimeClassification
    """The operational times of the school."""
    entrance_period:   EntrancePeriod
    """The entrance period of the school."""
    students_sex:      StudentsSex
    """The gender composition of the school's student body."""
    industry_supports: bool
    """Whether the school has industry support programs."""
    region:            Region
    """The region where the school is located."""
    address:           Optional[str]
    """The address of the school."""
    address_detail:    Optional[str]
    """The address details of the school."""
    zip_code:          int
    """The zip code of the school."""
    jurisdiction_name: str
    """The name of the jurisdiction overseeing the school."""
    tel_number:        str
    """The telephone number of the school."""
    fax_number:        Optional[str]
    """The fax number of the school."""
    website:           Optional[str]
    """The website of the school."""
    found_date:        date
    """The founding date of the school."""
    anniversary:       date
    """The anniversary date of the school."""
