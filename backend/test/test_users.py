from fastapi.testclient import TestClient

from api.main import app


client = TestClient(app)


def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == [{
        "id": "645951fc1363d9936cb4f8ea",
        "name": "Lola",
        "surname": "García",
        "age": 35
    }]
