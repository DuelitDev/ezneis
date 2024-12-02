# -*- coding: utf-8 -*-


__all__ = [
    "InternalServiceError",
    "ServiceUnavailableError",
    "DataNotFoundException",
    "SessionClosedException",
]


class InternalServiceError(Exception):
    def __init__(self, code: str, message: str):
        self._code = code
        self._message = message

    def __str__(self) -> str:
        return f"[{self._code}]: {self._message}"

    @property
    def code(self) -> str:
        return self._code

    @property
    def message(self) -> str:
        return self._message


class ServiceUnavailableError(Exception):
    def __init__(self, url: str):
        self._url = url

    def __str__(self) -> str:
        return f"Failed to connect to endpoint: {self._url}"

    @property
    def url(self) -> str:
        return self._url


class DataNotFoundException(Exception):
    def __init__(self, message: str = ""):
        super().__init__(message)


class SessionClosedException(IOError):
    def __str__(self) -> str:
        return "The session is closed."
