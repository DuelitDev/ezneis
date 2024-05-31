from abc import ABCMeta, abstractmethod
from ezneis.exception import *
from typing import Any

__all__ = [
    "Parser"
]


class Parser(metaclass=ABCMeta):
    _parsers = []

    @classmethod
    @abstractmethod
    def parse(cls, data) -> Any:
        """

        :param data:
        :return:
        """
        pass

    @classmethod
    def _run_parsers(cls, r) -> Any:
        """

        :param r:
        :return:
        """
        exceptions = []
        for parser in cls._parsers:
            try:
                return parser(r)
            except Exception as e:
                exceptions.append(e)
        raise ParseError(tuple(exceptions))