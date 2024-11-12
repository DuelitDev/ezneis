# -*- coding: utf-8 -*-
from dataclasses import dataclass
from datetime import date
from enum import Enum, auto
from typing import Optional
from ..utils.region import Region

__all__ = [
    "AdmissionPeriod",
    "FoundationType",
    "GenderComposition",
    "HighSchoolCategory",
    "HighSchoolSubtype",
    "SchoolCategory",
    "SchoolInfo",
    "SchoolPurpose",
    "SchoolTiming",
]


class FoundationType(Enum):
    """
    Types of school foundations.
    """
    PUBLIC      = auto()
    """A public school."""
    PRIVATE     = auto()
    """A private school."""


class SchoolCategory(Enum):
    """
    Types of schools.
    """
    ELEMENTARY = auto()
    """An elementary school."""
    MIDDLE     = auto()
    """A middle school."""
    HIGH       = auto()
    """A high school."""
    SEC_MID    = auto()
    """An open secondary middle school."""
    SEC_HIGH   = auto()
    """An open secondary high school."""
    MISC_ELE   = auto()
    """A miscellaneous elementary school."""
    MISC_MID   = auto()
    """A miscellaneous middle school."""
    MISC_HIGH  = auto()
    """A miscellaneous high school."""
    SPECIAL    = auto()
    """A special school."""
    OTHERS     = auto()
    """Other types of schools not listed."""


class HighSchoolCategory(Enum):
    """
    Types of high schools.
    """
    NORMAL     = auto()
    """A normal high school."""
    VOCATIONAL = auto()
    """A vocational high school."""


class HighSchoolSubtype(Enum):
    """
    Subtypes of high schools.
    """
    NORMAL          = auto()
    """A normal high school."""
    SPECIALIZED     = auto()
    """A specialized high school."""
    SPECIAL_PURPOSE = auto()
    """A special purpose high school."""
    AUTONOMOUS      = auto()
    """An autonomous high school."""
    OTHERS          = auto()
    """Other types of high schools not listed."""


class SchoolPurpose(Enum):
    """
    Primary purposes of schools.
    """
    INTERNATIONAL = auto()
    """A school with an international focus."""
    PHYSICAL      = auto()
    """A school with a focus on physical education."""
    ART           = auto()
    """A school with an art focus."""
    SCIENCE       = auto()
    """A school with a science focus."""
    LANGUAGE      = auto()
    """A school with a language focus."""
    INDUSTRY      = auto()
    """A school with an industry focus."""


class SchoolTiming(Enum):
    """
    School operational times.
    """
    DAY   = auto()
    """Operates during the daytime."""
    NIGHT = auto()
    """Operates during the nighttime."""
    BOTH  = auto()
    """Operates during both daytime and nighttime."""


class AdmissionPeriod(Enum):
    """
    School admission periods.
    """
    EARLY = auto()
    """Early admission period."""
    LATE  = auto()
    """Late admission period."""
    BOTH  = auto()
    """Both early and late admission periods."""


class GenderComposition(Enum):
    """
    Gender composition of the students.
    """
    MIXED      = auto()
    """A mixed-gender school."""
    BOYS_ONLY  = auto()
    """A boys-only school."""
    GIRLS_ONLY = auto()
    """A girls-only school."""


@dataclass(frozen=True)
class SchoolInfo:
    """
    Detailed information about a school.
    """
    code: str
    """The unique code of the school."""
    name: str
    """The name of the school."""
    english_name: Optional[str]
    """The English name of the school."""
    foundation_type: Optional[FoundationType]
    """The foundation type of the school."""
    school_category: SchoolCategory
    """The category of the school."""
    high_school_category: Optional[HighSchoolCategory]
    """The high school category if applicable."""
    subtype: Optional[HighSchoolSubtype]
    """The subtype of the high school if applicable."""
    purpose: Optional[SchoolPurpose]
    """The primary purpose of the school."""
    timing: SchoolTiming
    """The operational times of the school."""
    admission_period: AdmissionPeriod
    """The admission period of the school."""
    gender_composition: GenderComposition
    """The gender composition of the school's students."""
    industry_supports: bool
    """Indicates if the school has industry support programs."""
    region: Region
    """The region where the school is located."""
    address: Optional[str]
    """The address of the school."""
    address_detail: Optional[str]
    """Additional address details of the school."""
    zip_code: int
    """The zip code of the school."""
    jurisdiction_name: str
    """The name of the jurisdiction overseeing the school."""
    tel_number: str
    """The telephone number of the school."""
    fax_number: Optional[str]
    """The fax number of the school."""
    website: Optional[str]
    """The website of the school."""
    founded_date: date
    """The founding date of the school."""
    anniversary: date
    """The anniversary date of the school."""
