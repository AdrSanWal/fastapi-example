from pytest import fixture
from fastapi.testclient import TestClient

from api.main import app
from api.settings import settings
from db.client import client as mongoclient


@fixture()
def test_client():
    with TestClient(app) as client:
        db_name = settings._db
        settings._db = f"test_{db_name}"
        yield client
        mongoclient.drop_database(f"test_{db_name}")
        settings._db = db_name


@fixture()
def test_user():
    new_user = {
        "name": "Test user",
        "image": "default.jpg",
        "surname": "Test surname",
        "age": 40
    }
    return new_user


@fixture()
def test_user_updated():
    updated_user = {
        "name": "Test user updated",
        "image": "default.jpg",
        "surname": "Test surname updated",
        "age": 50
    }
    return updated_user


@fixture()
def test_collection():
    new_collection = {
        "model": "Test model updated",
        "title": "Test title updated",
        "relation": "http://www.test-url-updated.com",
        "address": {
            "locality": "TEST UPDATED",
            "postal_code": "28020",
            "street": "TEST STREET UPDATED"
        },
        "location": {
            "lat": 41.395212860537896,
            "lng": -4.722633997992097
        },
        "organization": {
            "name": "Test name updated",
            "description": "Test description updated",
            "schedule": "Test schedule updated",
            "services": "Test services updated"
        }
    }

    return new_collection


@fixture()
def test_collection_updated():
    updated_collection = {
        "model": "Test model",
        "title": "Test title",
        "relation": "http://www.test-url.com",
        "address": {
            "locality": "TEST",
            "postal_code": "28019",
            "street": "TEST STREET"
        },
        "location": {
            "lat": 40.395212860537896,
            "lng": -3.722633997992097
        },
        "organization": {
            "name": "Test name",
            "description": "Test description",
            "schedule": "Test schedule",
            "services": "Test services"
        }
    }

    return updated_collection
