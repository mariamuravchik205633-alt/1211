from app.main import app
from fastapi.testclient import TestClient


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
import os
import sys


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app