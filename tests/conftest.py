import pytest
from unsent.unsent import unsent

@pytest.fixture
def client():
    return unsent(key="test_api_key")
