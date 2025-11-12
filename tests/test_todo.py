from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_get():
    data = {"id": 1, "title": "Test task"}
    r = client.post("/todos", json=data)
    assert r.status_code == 200
    assert r.json()["title"] == "Test task"

    r = client.get("/todos")
    assert len(r.json()) == 1

def test_toggle():
    data = {"id": 2, "title": "Second"}
    client.post("/todos", json=data)
    r = client.patch("/todos/2")
    assert r.status_code == 200
    assert r.json()["done"] is True
