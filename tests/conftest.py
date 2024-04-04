import pytest
from logpacks.logger import Logger


@pytest.fixture
def logger():
    return Logger()
