import pytest
from fastapi.testclient import TestClient
from uuid import uuid4
from main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_root(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Hola"

def test_ids(client):
    id = 10
    response = client.get(f"id/{id}")

    assert response.status_code == 200
    assert response.json()["id"] == id