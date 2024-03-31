import pytest
from logpack.logger import Logger

@pytest.fixture
def logger():
    return Logger()