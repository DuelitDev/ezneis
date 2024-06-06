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
    Class NotExistException

    Exception class raised when something does not exist.
    """
    pass


class SchoolNotExistException(NotExistException):
    """
    Exception raised when the school does not exist.
    """
    pass


class AcademyNotExistException(NotExistException):
    """
    Exception raised when the academy does not exist.
    """
    pass


class DataNotExistException(NotExistException):
    """
    Exception raised when the requested data does not exist.
    """
    pass


class ParseException(Exception):
    """
    Exception class to encapsulate multiple exceptions raised during parsing.
    """
    def __init__(self, exceptions: Tuple[Exception, ...]):
        """
        Initialize the object with the given exceptions.

        :param exceptions: A tuple of exceptions to store.
        """
        self._exceptions = exceptions
        super().__init__(exceptions)

    @property
    def exceptions(self) -> Tuple[Exception, ...]:
        """
        :return: A tuple of exceptions that may be raised by the method.
        """
        return self._exceptions
