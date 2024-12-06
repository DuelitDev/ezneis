# -*- coding: utf-8 -*-
import atexit
import asyncio
from ..http import SyncSession, AsyncSession
from ..wrappers import SyncWrapper, AsyncWrapper

__all__ = [
    "SessionManager"
]


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class SessionManager:
    """
    동기 및 비동기 Session Wrapper의 생명 주기를 관리합니다.

    Session Wrapper를 생성하고, 필요하지 않을 때 세션을 정리할 수 있습니다.
    또한, 프로그램 종료 시 자동으로 세션이 정리되도록 설계되어 있습니다.
    """
    def __init__(self):
        # 동기 Session 및 Wrapper
        self._sync_session = None
        self._sync_wrapper = None
        # 비동기 Session 및 Wrapper
        self._async_session = None
        self._async_wrapper = None
        # 프로그램 종료 시 Session 종료 등록
        atexit.register(self.cleanup)

    def __del__(self):
        # Session 종료
        self.cleanup()

    def get_sync_wrapper(self, key: str) -> SyncWrapper:
        """
        보관된 동기 Session Wrapper를 반환합니다.

        만약 생성된 열린 동기 Session Wrapper가 없다면,
        동기 Session Wrapper를 새로 생성합니다.

        :param key: 나이스 교육정보 개방 포털 API 키입니다.
        :return: SyncWrapper
        """
        if self._sync_session is None or self._sync_session.closed:
            self._sync_session = SyncSession(key)
            self._sync_wrapper = SyncWrapper(self._sync_session)
        return self._sync_wrapper

    def get_async_wrapper(self, key: str) -> AsyncWrapper:
        """
        보관된 비동기 Session Wrapper를 반환합니다.

        만약 생성된 열린 비동기 Session Wrapper가 없다면,
        비동기 Session Wrapper를 새로 생성합니다.

        :param key: 나이스 교육정보 개방 포털 API 키입니다.
        :return: AsyncWrapper
        """
        if self._async_session is None or self._async_session.closed:
            self._async_session = AsyncSession(key)
            self._async_wrapper = AsyncWrapper(self._async_session)
        return self._async_wrapper

    def cleanup(self):
        # 동기 Session Wrapper 종료
        if self._sync_session and not self._sync_session.closed:
            self._sync_session.close()
            self._sync_session = None
            self._sync_wrapper = None
        # 비동기 Session Wrapper 종료
        if self._async_session and not self._async_session.closed:
            # Event loop 가져오기 또는 생성
            try:
                loop = asyncio.get_running_loop()
            except RuntimeError:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
            asyncio.run_coroutine_threadsafe(self._async_session.close(), loop)
            self._async_session = None
            self._async_wrapper = None
