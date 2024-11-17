# -*- coding: utf-8 -*-
from dataclasses import dataclass
from enum import Enum
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
    PRESCHOOL  = "PRESCHOOL"
    """Preschool education."""
    ELEMENTARY = "ELEMENTARY"
    """Elementary school education."""
    MIDDLE     = "MIDDLE"
    """Middle school education."""
    HIGH       = "HIGH"
    """High school education."""
    SPECIALITY = "SPECIALITY"
    """Specialized courses not falling under traditional levels."""


class DetailedCourseType(Enum):
    """
    Represents specific types of detailed courses within a school.
    """
    NORMAL        = "NORMAL"
    """Standard education."""
    VOCATIONAL    = "VOCATIONAL"
    """Vocational education."""
    SPECIALIZED   = "SPECIALIZED"
    """Specialized education."""
    INTERNATIONAL = "INTERNATIONAL"
    """International curriculum."""
    BUSINESS      = "BUSINESS"
    """Business education."""
    COMMERCE      = "COMMERCE"
    """Commerce education."""
    TECHNICAL     = "TECHNICAL"
    """Technical education."""
    AGRICULTURE   = "AGRICULTURE"
    """Agriculture-focused education."""
    FISHERIES     = "FISHERIES"
    """Fisheries-related courses."""
    INTEGRATED    = "INTEGRATED"
    """Integrated education programs."""
    LANGUAGE      = "LANGUAGE"
    """Language-focused education."""
    SCIENCE       = "SCIENCE"
    """Science-focused education."""
    PHYSICAL      = "PHYSICAL"
    """Physical education."""
    ART           = "ART"
    """Art-focused education."""
    ALTERNATIVE   = "ALTERNATIVE"
    """Alternative education programs."""
    TRAINING      = "TRAINING"
    """Training-specific courses."""


class ClassSchedule(Enum):
    """
    Represents the classification of a class based on timing.
    """
    DAY   = "DAY"
    """Daytime classes."""
    NIGHT = "NIGHT"
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
