from datetime import date
from enum import Enum, auto
from pydantic import BaseModel
from typing import Optional, SupportsIndex, Union

__all__ = [
    "ScheduleTimeClassification",
    "EventType",
    "EventCorresponds",
    "SchoolSchedule"
]


class ScheduleTimeClassification(Enum):
    """
    Enumeration representing the classification of a schedule based on time.
    """
    DAY   = auto()
    """Represents a daytime schedule."""
    NIGHT = auto()
    """Represents a nighttime schedule."""
    NONE  = auto()
    """Represents no specific time classification."""


class EventType(Enum):
    """
    Enumeration representing the type of event.
    """
    DAY_OFF = auto()
    """Represents that the event is a day off."""
    HOLIDAY = auto()
    """Represents that the event is a holiday."""
    NONE    = auto()
    """Represents that the event does not have a specified type."""


class EventCorresponds(BaseModel):
    """
    Model that represents that grade an event corresponds to.
    """
    grade0: bool
    """Represents if the event corresponds to 0th grade."""
    grade1: bool
    """Represents if the event corresponds to 1st grade."""
    grade2: bool
    """Represents if the event corresponds to 2nd grade."""
    grade3: bool
    """Represents if the event corresponds to 3rd grade."""
    grade4: bool
    """Represents if the event corresponds to 4th grade."""
    grade5: bool
    """Represents if the event corresponds to 5th grade."""
    grade6: bool
    """Represents if the event corresponds to 6th grade."""
    grade7: bool
    """Represents if the event corresponds to 7th grade."""

    def __getitem__(self, indices: Union[slice, SupportsIndex]):
        """
        Enables indexing and slicing to access grade correspondence.

        :param indices: Index or slice to access specific grades.
        :return: Tuple of booleans indicating
                 correspondence to specified grades.
        """
        return (self.grade0, self.grade1, self.grade2, self.grade3,
                self.grade4, self.grade5, self.grade6, self.grade7)[indices]


class SchoolSchedule(BaseModel):
    """
    Model representing a school schedule event.
    """
    year:        int
    """The year of the event."""
    time:        ScheduleTimeClassification
    """The time classification of the event."""
    name:        str
    """The name of the event."""
    description: Optional[str]
    """The description of the event."""
    corresponds: EventCorresponds
    """The model that represents that grade an event corresponds to."""
    type:        EventType
    """The type of the event."""
    date:        date
    """The date of the event."""

