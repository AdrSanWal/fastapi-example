from dotenv import load_dotenv, find_dotenv, set_key
from os import environ
import pytest
from fastapi.testclient import TestClient

from ..api.main import app
from ..api.settings import settings
from ..db.client import client as mongoclient


@pytest.fixture()
def test_client():
    with TestClient(app) as client:
        db_name = settings._db
        settings._db = f'test_{db_name}'
        yield client
        mongoclient.drop_database(f'test_{db_name}')
        settings._db = db_name


@pytest.fixture()
def test_user():
    new_user = {
        "name": "Test user",
        "surname": "Test surname",
        "age": 40
    }
    return new_user


@pytest.fixture()
def test_user_updated():
    new_user = {
        "name": "Test user updated",
        "surname": "Test surname updated",
        "age": 50
    }
    return new_user
