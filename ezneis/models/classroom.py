# -*- coding: utf-8 -*-
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional

__all__ = [
    "ClassSchedule",
    "Classroom",
    "CourseType",
    "DetailedCourseType",
]


class CourseType(Enum):
    """
    Represents different levels of school courses.
    """
    PRESCHOOL  = auto()
    """Preschool education."""
    ELEMENTARY = auto()
    """Elementary school education."""
    MIDDLE     = auto()
    """Middle school education."""
    HIGH       = auto()
    """High school education."""
    SPECIALITY = auto()
    """Specialized courses not falling under traditional levels."""


class DetailedCourseType(Enum):
    """
    Represents specific types of detailed courses within a school.
    """
    NORMAL        = auto()
    """Standard education."""
    VOCATIONAL    = auto()
    """Vocational education."""
    SPECIALIZED   = auto()
    """Specialized education."""
    INTERNATIONAL = auto()
    """International curriculum."""
    BUSINESS      = auto()
    """Business education."""
    COMMERCE      = auto()
    """Commerce education."""
    TECHNICAL     = auto()
    """Technical education."""
    AGRICULTURE   = auto()
    """Agriculture-focused education."""
    FISHERIES     = auto()
    """Fisheries-related courses."""
    INTEGRATED    = auto()
    """Integrated education programs."""
    LANGUAGE      = auto()
    """Language-focused education."""
    SCIENCE       = auto()
    """Science-focused education."""
    PHYSICAL      = auto()
    """Physical education."""
    ART           = auto()
    """Art-focused education."""
    ALTERNATIVE   = auto()
    """Alternative education programs."""
    TRAINING      = auto()
    """Training-specific courses."""


class ClassSchedule(Enum):
    """
    Represents the classification of a class based on timing.
    """
    DAY   = auto()
    """Daytime classes."""
    NIGHT = auto()
    """Nighttime classes."""


@dataclass(frozen=True)
class Classroom:
    """
    Represents information about a class.
    """
    year: int
    """The year the class is conducted."""
    grade: int
    """The grade level of the class."""
    name: Optional[str]
    """The name of the class."""
    department: Optional[str]
    """The department offering the class."""
    course: CourseType
    """The type of course."""
    course_detail: Optional[DetailedCourseType]
    """The detailed type of course."""
    timing: Optional[ClassSchedule]
    """The time classification of the class."""
