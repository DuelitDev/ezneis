# -*- coding: utf-8 -*-
import atexit
import asyncio
from ..http import SyncSession, AsyncSession
from ..wrappers import SyncWrapper, AsyncWrapper

__all__ = [
    "SessionManager"
]


class SessionManager:
    def __init__(self):
        self._sync_session = None
        self._sync_wrapper = None
        self._async_session = None
        self._async_wrapper = None
        atexit.register(self.cleanup)

    def get_sync_wrapper(self, key: str) -> SyncWrapper:
        if self._sync_session is None or self._sync_session.closed:
            self._sync_session = SyncSession(key)
            self._sync_wrapper = SyncWrapper(self._sync_session)
        return self._sync_wrapper

    def get_async_wrapper(self, key: str) -> AsyncWrapper:
        if self._async_session is None or self._async_session.closed:
            self._async_session = AsyncSession(key)
            self._async_wrapper = AsyncWrapper(self._async_session)
        return self._async_wrapper

    def cleanup(self):
        if self._sync_session and not self._sync_session.closed:
            self._sync_session.close()
            self._sync_session = None
            self._sync_wrapper = None
        if self._async_session and not self._async_session.closed:
            try:
                loop = asyncio.get_event_loop()
            except RuntimeError:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
            asyncio.run_coroutine_threadsafe(self._async_session.close(), loop)
            self._async_session = None
            self._async_wrapper = None

    def __del__(self):
        self.cleanup()