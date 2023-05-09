import json

#from .conftest import test_client


def test_get_users(test_client):
    response = test_client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert True


def test_post_user(test_client, test_db):
    new_user = {
        "name": "Test user",
        "surname": "Test surname",
        "age": 40
    }
    response = test_client.post("/users", data=json.dumps(new_user))
    assert response.status_code == 201
    print(response.json)
    assert False
