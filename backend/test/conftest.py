import pytest
from fastapi.testclient import TestClient

from ..api.main import app
from ..api.settings import Settings


@pytest.fixture()
def test_client():
    with TestClient(app) as client:
        yield client
