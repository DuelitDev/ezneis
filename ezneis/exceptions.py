# -*- coding: utf-8 -*-
from enum import Enum


__all__ = [
    "InternalServiceCode",
    "InternalServiceError",
    "ServiceUnavailableError",
    "DataNotFoundException",
    "SessionClosedException",
]


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class InternalServiceCode(Enum):
    """
    내부 서비스 오류에 대한 코드 열거형입니다.
    """
    OK                = "INFO-000"
    """정상 처리되었습니다."""
    REFERENCE_ONLY    = "INFO-100"
    """해당 자료는 단순 참고용으로만 활용하시기 바랍니다."""
    NOT_FOUND         = "INFO-200"
    """해당하는 데이터가 없습니다."""
    FORBIDDEN         = "INFO-300"
    """관리자에 의해 인증키 사용이 제한되었습니다."""
    BAD_REQUEST       = "ERROR-300"
    """필수 값이 누락되어 있습니다. 
       요청인자를 참고 하십시오."""
    UNAUTHORIZED      = "ERROR-290"
    """인증키가 유효하지 않습니다. 인증키가 없는 경우, 
       홈페이지에서 인증키를 신청하십시오."""
    UNKNOWN_SERVICE   = "ERROR-310"
    """해당하는 서비스를 찾을 수 없습니다. 
       요청인자 중 SERVICE를 확인하십시오."""
    UNSUPPORTED_TYPE  = "ERROR-333"
    """요청위치 값의 타입이 유효하지 않습니다.
       요청위치 값은 정수를 입력하세요."""
    REQUEST_TOO_LARGE = "ERROR-336"
    """데이터요청은 한번에 최대 1,000건을 넘을 수 없습니다."""
    TOO_MANY_REQUESTS = "ERROR-337"
    """일별 트래픽 제한을 넘은 호출입니다. 
       오늘은 더이상 호출할 수 없습니다."""
    SERVER_ERROR      = "ERROR-500"
    """서버 오류입니다. 
       지속적으로 발생시 홈페이지로 문의(Q&A) 바랍니다."""
    DATABASE_ERROR    = "ERROR-600"
    """데이터베이스 연결 오류입니다. 
       지속적으로 발생시 홈페이지로 문의(Q&A) 바랍니다."""
    SQL_SYNTAX_ERROR  = "ERROR-601"
    """SQL 문장 오류 입니다. 
       지속적으로 발생시 홈페이지로 문의(Q&A) 바랍니다."""


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class InternalServiceError(Exception):
    """
    요청한 서비스의 데이터에 발생한 오류를 나타냅니다.
    """

    def __init__(self, code: str, message: str):
        self._code = InternalServiceCode(code)
        self._message = message

    def __str__(self) -> str:
        return f"[{self._code}]: {self._message}"

    @property
    def code(self) -> InternalServiceCode:
        """
        내부 서비스 오류에 대한 코드입니다.

        :return: InternalServiceCode
        """
        return self._code

    @property
    def message(self) -> str:
        """
        내부 서비스 오류에 대한 설명입니다.

        :return: str
        """
        return self._message


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class ServiceUnavailableError(Exception):
    """
    서비스 요청에 실패했을 때 발생한 오류를 나타냅니다.
    """

    def __init__(self, url: str):
        self._url = url

    def __str__(self) -> str:
        return f"Endpoint에 연결 실패: {self._url}"

    @property
    def url(self) -> str:
        """
        요청한 서비스의 url입니다.

        :return: str
        """
        return self._url


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class DataNotFoundException(Exception):
    """
    서비스 데이터가 없는 예외를 나타냅니다.
    """

    def __init__(self, message: str = ""):
        super().__init__(message)


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class SessionClosedException(IOError):
    """
    사용하려는 세션이 이미 닫힌 예외를 나타냅니다.
    """

    def __str__(self) -> str:
        return "이 세션은 이미 닫혔습니다."
