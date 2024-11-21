# -*- coding: utf-8 -*-
from typing import Optional
from .data.school import SyncSchoolData, AsyncSchoolData
from .http import SyncSession, AsyncSession
from .wrappers import SyncWrapper, AsyncWrapper
from .utils.region import Region


def fetch_school(key: str, name: str, region: Optional[Region] = None
                 ) -> SyncSchoolData:
    with SyncSession(key) as session:
        wrapper = SyncWrapper(session)
        info = wrapper.get_school_info(name, region, hint=1)
        if not info:
            # TODO: Data not found.
            raise "No Data."
        return SyncSchoolData(key, info=info[0])


def fetch_schools(key: str, name: str, region: Optional[Region] = None
                  ) -> tuple[SyncSchoolData, ...]:
    with SyncSession(key) as session:
        wrapper = SyncWrapper(session)
        info = wrapper.get_school_info(name, region)
        return tuple(SyncSchoolData(key, info=i) for i in info)


async def fetch_school_async(key: str, name: str,
                             region: Optional[Region] = None
                             ) -> AsyncSchoolData:
    async with AsyncSession(key) as session:
        wrapper = AsyncWrapper(session)
        info = await wrapper.get_school_info(name, region, hint=1)
        if not info:
            # TODO: Data not found.
            raise "No Data."
        return AsyncSchoolData(key, info=info[0])


async def fetch_schools_async(key: str, name: str,
                              region: Optional[Region] = None
                              ) -> tuple[AsyncSchoolData, ...]:
    async with AsyncSession(key) as session:
        wrapper = AsyncWrapper(session)
        info = await wrapper.get_school_info(name, region)
        return tuple(AsyncSchoolData(key, info=i) for i in info)

