import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_activity():
    response = client.post(
        "/activities/", json={"name": "Test Activity", "description": "Test Description"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Activity"
    assert data["description"] == "Test Description"
    assert "id" in data


def test_read_activity():
    # First, create an activity
    create_response = client.post(
        "/activities/", json={"name": "Test Activity", "description": "Test Description"}
    )
    assert create_response.status_code == 200
    created_activity = create_response.json()
    activity_id = created_activity["id"]

    # Then, read the activity
    read_response = client.get(f"/activities/{activity_id}")
    assert read_response.status_code == 200
    read_activity = read_response.json()
    assert read_activity["id"] == activity_id
    assert read_activity["name"] == "Test Activity"
    assert read_activity["description"] == "Test Description"


def test_read_activity_not_found():
    response = client.get("/activities/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_update_activity():
    # First, create an activity
    create_response = client.post(
        "/activities/", json={"name": "Test Activity", "description": "Test Description"}
    )
    assert create_response.status_code == 200
    created_activity = create_response.json()
    activity_id = created_activity["id"]

    # Then, update the activity
    update_response = client.put(
        f"/activities/{activity_id}",
        json={"name": "Updated Activity", "description": "Updated Description"},
    )
    assert update_response.status_code == 200
    updated_activity = update_response.json()
    assert updated_activity["id"] == activity_id
    assert updated_activity["name"] == "Updated Activity"
    assert updated_activity["description"] == "Updated Description"


def test_delete_activity():
    # First, create an activity
    create_response = client.post(
        "/activities/", json={"name": "Test Activity", "description": "Test Description"}
    )
    assert create_response.status_code == 200
    created_activity = create_response.json()
    activity_id = created_activity["id"]

    # Then, delete the activity
    delete_response = client.delete(f"/activities/{activity_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "Activity deleted successfully"}

    # Verify that the activity is deleted
    read_response = client.get(f"/activities/{activity_id}")
    assert read_response.status_code == 404
\`\`\`
