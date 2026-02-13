"""Unit tests for application."""
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_read_main():
    """Test root endpoint returns Hello, World."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_item():
    """Test item endpoint returns correct item_id."""
    response = client.get("/items/42?item_count=10")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "10"}


def test_read_item_no_query():
    """Test item endpoint without optional query param."""
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": None}
