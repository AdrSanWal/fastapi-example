from dotenv import load_dotenv, find_dotenv, set_key
from os import environ
import pytest
from fastapi.testclient import TestClient

from ..api.main import app
from ..api.settings import Settings
from ..db.client import client as mongoclient


@pytest.fixture()
def test_client():
    with TestClient(app) as client:
        settings = Settings
        settings._db = 'test_db'
        yield client
        mongoclient.drop_database('test_db')


@pytest.fixture()
def user_1():
    new_user = {
        "name": "Test user",
        "surname": "Test surname",
        "age": 40
    }
    return new_user
