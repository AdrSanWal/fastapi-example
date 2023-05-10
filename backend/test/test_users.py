import json


def test_get_users(test_client):
    response = test_client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_post_user(test_client, user_1):
    response = test_client.post("/users", content=json.dumps(user_1))
    assert response.status_code == 201


def test_post_existing_user(test_client, user_1):
    test_client.post("/users", content=json.dumps(user_1))
    response = test_client.post("/users", content=json.dumps(user_1))
    assert response.status_code == 409
