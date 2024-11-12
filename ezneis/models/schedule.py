# -*- coding: utf-8 -*-
from dataclasses import dataclass
from datetime import date
from enum import Enum, auto
from typing import Optional, SupportsIndex

__all__ = [
    "GradeCorrespondence",
    "ScheduleTime",
    "ScheduleType",
    "SchoolSchedule",
]


class ScheduleTime(Enum):
    """
    Enumeration representing the time classification of a schedule.
    """
    DAY   = auto()
    """Represents a day schedule."""
    NIGHT = auto()
    """Represents a night schedule."""


class ScheduleType(Enum):
    """
    Enumeration representing the category of a schedule.
    """
    DAY_OFF = auto()
    """Represents a day off event."""
    HOLIDAY = auto()
    """Represents a holiday event."""


@dataclass(frozen=True)
class GradeCorrespondence:
    """
    Model representing the grades to which a schedule corresponds.
    """
    grade0: bool
    """Indicates if the schedule corresponds to grade 0."""
    grade1: bool
    """Indicates if the schedule corresponds to grade 1."""
    grade2: bool
    """Indicates if the schedule corresponds to grade 2."""
    grade3: bool
    """Indicates if the schedule corresponds to grade 3."""
    grade4: bool
    """Indicates if the schedule corresponds to grade 4."""
    grade5: bool
    """Indicates if the schedule corresponds to grade 5."""
    grade6: bool
    """Indicates if the schedule corresponds to grade 6."""
    grade7: bool
    """Indicates if the schedule corresponds to grade 7."""

    def __getitem__(self, indices: slice | SupportsIndex):
        """
        Allows indexing and slicing to access grade correspondence.

        :param indices: Index or slice to access specific grades.
        :return: Tuple of booleans indicating correspondence
                 to specified grades.
        """
        return (self.grade0, self.grade1, self.grade2, self.grade3,
                self.grade4, self.grade5, self.grade6, self.grade7)[indices]


@dataclass(frozen=True)
class SchoolSchedule:
    """
    Model representing a school schedule event.
    """
    year: int
    """The year of the event."""
    time: Optional[ScheduleTime]
    """The time classification of the event."""
    name: str
    """The name of the event."""
    description: Optional[str]
    """The description of the event."""
    correspondence: GradeCorrespondence
    """The model representing the grades to which the event corresponds."""
    type: Optional[ScheduleType]
    """The type of the event."""
    date: date
    """The date of the event."""
