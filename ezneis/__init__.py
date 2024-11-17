# -*- coding: utf-8 -*-
from typing import Optional
from .data.school.synchronous import SyncSchoolData
from .http import SyncSession, AsyncSession
from .wrappers import SyncWrapper, AsyncWrapper
from .utils.region import Region


def fetch(key: str, name: str, region: Optional[Region] = None):
    with SyncSession(key) as session:
        wrapper = SyncWrapper(session)
        info = wrapper.get_school_info(name, region)[0]
        return SyncSchoolData(key, info=info)

