# -*- coding: utf-8 -*-
"""
모델 코어 모듈

이 모듈은 NEIS Open API를 통해 데이터를 조회하는 모델의 기본 클래스를 제공합니다.
CoreModel 클래스는 모든 모델 클래스의 기본이 되는 추상 클래스이며,
CoreBuilder 클래스는 API 쿼리를 구성하는 빌더 클래스의 기본이 되는 추상 클래스입니다.

**사용례**::

    # 이 모듈은 직접 사용하지 않고, 하위 클래스를 통해 사용합니다.
    # 예를 들어, SchoolInfo와 SchoolInfoBuilder 클래스는 이 모듈의 클래스를 상속받습니다.

    from ezneis import SyncSession
    from ezneis.models import SchoolInfoBuilder

    # 빌더를 사용하여 쿼리 구성
    builder = SchoolInfoBuilder()

    # 세션을 통해 데이터 조회
    session = SyncSession("API_KEY")
    schools = builder >> session
"""
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Awaitable, Sequence
from ..http import AsyncSession, Service, SyncSession

__all__ = ["CoreModel", "CoreBuilder"]


@dataclass(frozen=True)
class CoreModel(metaclass=ABCMeta):
    """
    모든 모델 클래스의 기본이 되는 추상 클래스입니다.

    이 클래스는 NEIS Open API에서 제공하는 데이터를 표현하는 모델 클래스의 기본이 됩니다.
    모든 모델 클래스는 이 클래스를 상속받아야 합니다.
    """

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict) -> CoreModel:
        """
        API 응답 데이터로부터 모델 객체를 생성합니다.

        :param data: NEIS Open API의 응답 데이터
        :type data: dict
        :return: 생성된 모델 객체
        :rtype: CoreModel
        """
        pass


class CoreBuilder(metaclass=ABCMeta):
    """
    API 쿼리를 구성하는 빌더 클래스의 기본이 되는 추상 클래스입니다.

    이 클래스는 NEIS Open API에 대한 쿼리를 구성하는 데 사용됩니다.
    메서드 체이닝을 통해 쿼리 파라미터를 설정하고, 연산자 오버로딩(>>)을 통해 데이터를 조회할 수 있습니다.
    모든 빌더 클래스는 이 클래스를 상속받아야 합니다.
    """

    def __init__(self):
        """
        CoreBuilder 인스턴스를 초기화합니다.

        파라미터 딕셔너리와 제한 값을 초기화합니다.
        """
        self._param = {}
        self._limit: int | None = None

    def __copy__(self):
        """
        빌더의 복사본을 생성합니다.

        :return: 현재 빌더의 복사본
        :rtype: CoreBuilder
        """
        new = self.__class__()
        new._param = self._param.copy()
        return new

    def copy(self) -> CoreBuilder:
        """
        빌더의 복사본을 생성합니다.

        :return: 현재 빌더의 복사본
        :rtype: CoreBuilder
        """
        return self.__copy__()

    def reset(self) -> CoreBuilder:
        """
        빌더의 파라미터를 초기화합니다.

        :return: 파라미터가 초기화된 빌더 인스턴스
        :rtype: CoreBuilder
        """
        self._param.clear()
        return self

    @property
    @abstractmethod
    def _service(self) -> Service:
        """
        사용할 NEIS Open API 서비스를 반환합니다.

        :return: 사용할 NEIS Open API 서비스
        :rtype: Service
        """
        pass

    @property
    @abstractmethod
    def _model(self) -> type[CoreModel]:
        """
        API 응답을 변환할 모델 클래스를 반환합니다.

        :return: 사용할 모델 클래스
        :rtype: type[CoreModel]
        """
        pass

    def __rshift__(
        self, other: AsyncSession | SyncSession
    ) -> Sequence[CoreModel] | Awaitable[Sequence[CoreModel]]:
        """
        >> 연산자를 통해 세션에서 데이터를 조회합니다.

        :param other: 데이터를 조회할 세션
        :type other: AsyncSession 또는 SyncSession
        :return: 조회된 모델 객체의 시퀀스 또는 비동기 작업
        :rtype: Sequence[CoreModel] 또는 Awaitable[Sequence[CoreModel]]
        :raises TypeError: 지원되지 않는 타입의 세션이 전달된 경우
        """
        if isinstance(other, SyncSession):
            return self.fetch(other)
        elif isinstance(other, AsyncSession):
            return self.fetch_async(other)
        raise TypeError(f"unsupported operand type(s) for >>: '{type(other)}'")

    def fetch(self, sess: SyncSession) -> Sequence[CoreModel]:
        """
        동기 세션을 사용하여 데이터를 조회합니다.

        :param sess: 데이터를 조회할 동기 세션
        :type sess: SyncSession
        :return: 조회된 모델 객체의 시퀀스
        :rtype: Sequence[CoreModel]
        """
        return tuple(
            self._model.from_dict(i)
            for i in sess.get(self._service, limit=self._limit, **self._param)
        )

    async def fetch_async(self, sess: AsyncSession) -> Sequence[CoreModel]:
        """
        비동기 세션을 사용하여 데이터를 조회합니다.

        :param sess: 데이터를 조회할 비동기 세션
        :type sess: AsyncSession
        :return: 조회된 모델 객체의 시퀀스
        :rtype: Sequence[CoreModel]
        """
        return tuple(
            self._model.from_dict(i)
            for i in await sess.get(self._service, limit=self._limit, **self._param)
        )

    @abstractmethod
    def __rrshift__(self, other) -> CoreBuilder:
        """
        << 연산자를 통해 다른 객체로부터 파라미터를 상속받습니다.

        :param other: 파라미터를 상속받을 객체
        :type other: Any
        :return: 파라미터가 업데이트된 빌더 인스턴스
        :rtype: CoreBuilder
        """
        pass

    def limit(self, limit: int) -> CoreBuilder:
        """
        조회할 최대 레코드 수를 설정합니다.

        :param limit: 조회할 최대 레코드 수
        :type limit: int
        :return: 메서드 체이닝을 위한 빌더 인스턴스
        :rtype: CoreBuilder
        """
        self._limit = limit
        return self
