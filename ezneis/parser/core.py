from abc import ABCMeta, abstractmethod
from ezneis.exception import *
from typing import Any

__all__ = [
    "Parser"
]


class Parser(metaclass=ABCMeta):
    """
    Abstract base class for parsers.

    This class serves as a blueprint for creating different parsers.
    The class also provides a mechanism for running multiple parsers
    on a given input, returning the result of the first successful parse.
    """
    _parsers = []

    @classmethod
    @abstractmethod
    def parse(cls, data) -> Any:
        """
        Parse the given data.

        :param data: The data to be parsed.
        :return: The parsed data.
        """
        pass

    @classmethod
    def _run_parsers(cls, r) -> Any:
        """
        Run parsers on a given input and returns
        the result of the first successful parsing.
        If all parsers fail, it raises a ParseException.

        :param r: The input to be parsed
        :return: The result of the successful parsing
        :raises ParseException: If all parsers fail to parse the input.
        """
        exceptions = []
        for parser in cls._parsers:
            try:
                return parser(r)
            except Exception as e:
                exceptions.append(e)
        raise ParseException(tuple(exceptions))
