from typing import Tuple

__all__ = [
    "NotExistException",
    "SchoolNotExistException",
    "AcademyNotExistException",
    "DataNotExistException",
    "ParseException"
]


class NotExistException(Exception):
    """

    """
    pass


class SchoolNotExistException(NotExistException):
    """

    """
    pass


class AcademyNotExistException(NotExistException):
    """

    """
    pass


class DataNotExistException(NotExistException):
    """

    """
    pass


class ParseException(Exception):
    """

    """
    def __init__(self, exceptions: Tuple[Exception, ...]):
        """

        :param exceptions:
        """
        self._exceptions = exceptions
        super().__init__(exceptions)

    @property
    def exceptions(self) -> Tuple[Exception, ...]:
        """

        :return:
        """
        return self._exceptions
