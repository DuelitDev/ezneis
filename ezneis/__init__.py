# -*- coding: utf-8 -*-
from typing import Optional
from .data.school import SyncSchoolData, AsyncSchoolData
from .exceptions import DataNotFoundException
from .http import SyncSession, AsyncSession
from .utils.region import Region
from .utils.session_manager import SessionManager
from .wrappers import SyncWrapper, AsyncWrapper

__all__ = [
    "fetch_school",
    "fetch_schools",
    "fetch_school_async",
    "fetch_schools_async",
    "SyncSession",
    "AsyncSession",
    "SyncWrapper",
    "AsyncWrapper",
    "SyncSchoolData",
    "AsyncSchoolData",
    "Region",
]


_session_manager = SessionManager()


def fetch_school(key: str, name: str, region: Optional[Region] = None
                 ) -> SyncSchoolData:
    wrapper = _session_manager.get_sync_wrapper(key)
    info = wrapper.get_school_info(name, region, hint=1)
    if not info:
        raise DataNotFoundException
    return SyncSchoolData(wrapper, info=info[0])


def fetch_schools(key: str, name: str, region: Optional[Region] = None
                  ) -> tuple[SyncSchoolData, ...]:
    wrapper = _session_manager.get_sync_wrapper(key)
    info = wrapper.get_school_info(name, region)
    return tuple(SyncSchoolData(wrapper, info=i) for i in info)


async def fetch_school_async(key: str, name: str,
                             region: Optional[Region] = None
                             ) -> AsyncSchoolData:
    wrapper = _session_manager.get_async_wrapper(key)
    info = await wrapper.get_school_info(name, region, hint=1)
    if not info:
        raise DataNotFoundException
    return AsyncSchoolData(wrapper, info=info[0])


async def fetch_schools_async(key: str, name: str,
                              region: Optional[Region] = None
                              ) -> tuple[AsyncSchoolData, ...]:
    wrapper = _session_manager.get_async_wrapper(key)
    info = await wrapper.get_school_info(name, region)
    return tuple(AsyncSchoolData(wrapper, info=i) for i in info)


def cleanup():
    _session_manager.cleanup()
