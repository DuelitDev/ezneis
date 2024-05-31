from typing import Tuple

__all__ = [
    "UnhandledError",
    "NotExistError",
    "SchoolNotExistError",
    "AcademyNotExistError",
    "DataNotExistError",
    "ParseError"
]


class UnhandledError(Exception):
    """

    """
    def __init__(self, exception: Exception):
        """

        :param exception:
        """
        super().__init__(exception)


class NotExistError(Exception):
    """

    """
    pass


class SchoolNotExistError(NotExistError):
    """

    """
    pass


class AcademyNotExistError(NotExistError):
    """

    """
    pass


class DataNotExistError(NotExistError):
    """

    """
    pass


class ParseError(Exception):
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
