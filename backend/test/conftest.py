from pytest import fixture
from fastapi.testclient import TestClient

from api.main import app
# from api.main import app
from api.settings import settings
from db.client import client as mongoclient


@fixture()
def test_client():
    with TestClient(app) as client:
        db_name = settings.db
        settings.db = f"test_{db_name}"
        yield client
        mongoclient.drop_database(f"test_{db_name}")
        settings.db = db_name


@fixture()
def test_user():
    new_user = {
        'user': {
            "email": "test_user@test.com",
            "name": "Test user",
            "surname": "Test surname",
            "password": "password",
            "password_confirm": "password",
            "age": 40,
            'is_active': True,
            'is_admin': False
        },
        'login': {
            "email": "test_user@test.com",
            "password": "password"
        }
    }
    return new_user


@fixture()
def test_admin():
    new_admin = {
        'user': {
            "email": "test_admin@test.com",
            "name": "Test admin",
            "surname": "Test surname",
            "password": "password",
            "password_confirm": "password",
            "age": 40,
            'is_active': True,
            'is_admin': True
        },
        'login': {
            "email": "test_admin@test.com",
            "password": "password"
        }
    }
    return new_admin


@fixture()
def test_user_updated():
    updated_user = {
        "name": "Test user updated",
        "surname": "Test surname updated",
        "password": "password",
        "age": 50,
        'is_active': True,
        'is_admin': False
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
