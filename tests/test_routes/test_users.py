import json


def test_create_user(client):
    data = {
        "username": "testuser",
        "email": "testuser@testing.com",
        "password": "testing"
    }
    response = client.post("/users/", json.dumps(data))

    assert response.status_code == 200
    assert response.json()["email"] == "testuser@testing.com"
    assert response.json()["is_active"] == True
