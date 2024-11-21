# -*- coding: utf-8 -*-
from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Optional
from .common import Timing
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
]


class FoundationType(Enum):
    """
    Types of school foundations.
    """
    PUBLIC      = "PUBLIC"
    """A public school."""
    PRIVATE     = "PRIVATE"
    """A private school."""


class SchoolCategory(Enum):
    """
    Types of schools.
    """
    ELEMENTARY = "ELEMENTARY"
    """An elementary school."""
    MIDDLE     = "MIDDLE"
    """A middle school."""
    HIGH       = "HIGH"
    """A high school."""
    SEC_MID    = "SEC_MID"
    """An open secondary middle school."""
    SEC_HIGH   = "SEC_HIGH"
    """An open secondary high school."""
    MISC_ELE   = "MISC_ELE"
    """A miscellaneous elementary school."""
    MISC_MID   = "MISC_MID"
    """A miscellaneous middle school."""
    MISC_HIGH  = "MISC_HIGH"
    """A miscellaneous high school."""
    SPECIAL    = "SPECIAL"
    """A special school."""
    OTHERS     = "OTHERS"
    """Other types of schools not listed."""


class HighSchoolCategory(Enum):
    """
    Types of high schools.
    """
    NORMAL     = "NORMAL"
    """A normal high school."""
    VOCATIONAL = "VOCATIONAL"
    """A vocational high school."""


class HighSchoolSubtype(Enum):
    """
    Subtypes of high schools.
    """
    NORMAL          = "NORMAL"
    """A normal high school."""
    SPECIALIZED     = "SPECIALIZED"
    """A specialized high school."""
    SPECIAL_PURPOSE = "SPECIAL_PURPOSE"
    """A special purpose high school."""
    AUTONOMOUS      = "AUTONOMOUS"
    """An autonomous high school."""
    OTHERS          = "OTHERS"
    """Other types of high schools not listed."""


class SchoolPurpose(Enum):
    """
    Primary purposes of schools.
    """
    INTERNATIONAL = "INTERNATIONAL"
    """A school with an international focus."""
    PHYSICAL      = "PHYSICAL"
    """A school with a focus on physical education."""
    ART           = "ART"
    """A school with an art focus."""
    SCIENCE       = "SCIENCE"
    """A school with a science focus."""
    LANGUAGE      = "LANGUAGE"
    """A school with a language focus."""
    INDUSTRY      = "INDUSTRY"
    """A school with an industry focus."""


class AdmissionPeriod(Enum):
    """
    School admission periods.
    """
    EARLY = "EARLY"
    """Early admission period."""
    LATE  = "LATE"
    """Late admission period."""
    BOTH  = "BOTH"
    """Both early and late admission periods."""


class GenderComposition(Enum):
    """
    Gender composition of the students.
    """
    MIXED      = "MIXED"
    """A mixed-gender school."""
    BOYS_ONLY  = "BOYS_ONLY"
    """A boys-only school."""
    GIRLS_ONLY = "GIRLS_ONLY"
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
    timing: Timing
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
