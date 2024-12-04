import pytest
from tests import get_key
from random import choice, sample
from ezneis.http import SyncSession
from ezneis.wrappers import SyncWrapper
from ezneis.utils.region import Region


@pytest.fixture(scope="package", autouse=True)
def region():
    return choice(list(Region))


@pytest.fixture(scope="package", autouse=True)
def schools(region):
    samples = 10
    with SyncSession(get_key()) as session:
        wrapper = SyncWrapper(session)
        info = wrapper.get_school_info("", region, hint=150)
        if len(info) < samples:
            return info
        return sample(info, 10)
