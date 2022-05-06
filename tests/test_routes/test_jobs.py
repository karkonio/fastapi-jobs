import json

from fastapi import status


def test_create_job(client, normal_user_token_headers):
    data = {
        "title": "Python developer",
        "company": "DataArt",
        "company_url": "dataart.kz",
        "location": "Kazakhstan, Almaty",
        "description": "python",
        "date_posted": "2022-04-04",
    }
    response = client.post(
        "/jobs/create-job/",
        json.dumps(data),
        headers=normal_user_token_headers,
    )
    assert response.status_code == 200
    assert response.json()["company"] == "DataArt"
    assert response.json()["description"] == "python"


def test_read_job(client, normal_user_token_headers):
    data = {
        "title": "Python developer",
        "company": "DataArt",
        "company_url": "dataart.kz",
        "location": "Kazakhstan, Almaty",
        "description": "python",
        "date_posted": "2022-04-04",
    }
    response = client.post(
        "/jobs/create-job/",
        json.dumps(data),
        headers=normal_user_token_headers,
    )

    response = client.get("/jobs/get/1/")
    assert response.status_code == 200
    assert response.json()["title"] == "Python developer"


def test_read_all_jobs(client, normal_user_token_headers):
    data = {
        "title": "Python developer",
        "company": "DataArt",
        "company_url": "dataart.kz",
        "location": "Kazakhstan, Almaty",
        "description": "python",
        "date_posted": "2022-04-04",
    }
    client.post(
        "/jobs/create-job/",
        json.dumps(data),
        headers=normal_user_token_headers,
    )
    client.post(
        "/jobs/create-job/",
        json.dumps(data),
        headers=normal_user_token_headers,
    )

    response = client.get("/jobs/all/")
    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]


def test_update_a_job(client, normal_user_token_headers):
    data = {
        "title": "Python developer",
        "company": "DataArt",
        "company_url": "dataart.kz",
        "location": "Kazakhstan, Almaty",
        "description": "python",
        "date_posted": "2022-04-04",
    }
    client.post(
        "/jobs/create-job/",
        json.dumps(data),
        headers=normal_user_token_headers,
    )

    data["title"] = "Java developer"
    response = client.put("/jobs/update/1", json.dumps(data))
    assert response.json()["msg"] == "Successfully updated data."


def test_delete_a_job(client, normal_user_token_headers):
    data = {
        "title": "Python developer",
        "company": "DataArt",
        "company_url": "dataart.kz",
        "location": "Kazakhstan, Almaty",
        "description": "python",
        "date_posted": "2022-04-04",
    }
    client.post(
        "/jobs/create-job/",
        json.dumps(data),
        headers=normal_user_token_headers,
    )
    client.delete("/jobs/delete/1", headers=normal_user_token_headers)
    response = client.get("/jobs/get/1/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
