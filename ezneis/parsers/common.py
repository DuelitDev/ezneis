# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from typing import Any

__all__ = [
    "Parser"
]


class Parser(metaclass=ABCMeta):
    """
    Abstract base class for parsers. This class serves as a blueprint for
    creating different parsers that can convert data between a dictionary
    (usually parsed from JSON) and a specified format or data structure.
    """

    @classmethod
    @abstractmethod
    def from_json(cls, data: dict) -> Any:
        """
        Parse the given dictionary into the appropriate data format.
        This method should be implemented by subclasses to define how the input
        dictionary should be transformed into the desired output format.

        :param data: The dictionary containing data to be parsed.
        :return: The parsed data in the desired output format.
        """
        pass
