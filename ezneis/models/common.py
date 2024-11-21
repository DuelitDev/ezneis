# -*- coding: utf-8 -*-
from enum import Enum

__all__ = [
    "Timing",
]


class Timing(Enum):
    """
    operational times.
    """
    DAY   = "DAY"
    """Operates during the daytime."""
    NIGHT = "NIGHT"
    """Operates during the nighttime."""
    BOTH  = "BOTH"
    """Operates during both daytime and nighttime."""

    def __contains__(self, item):
        if self is Timing.BOTH:
            return True
        return item == self
