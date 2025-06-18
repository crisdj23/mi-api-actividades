import pytest
import json
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_tasks(client):
    resp = client.get('/tasks')
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list)

def test_create_task(client):
    resp = client.post('/tasks', json={'title': 'Test tarea'})
    assert resp.status_code == 201
    data = resp.get_json()
    assert data['title'] == 'Test tarea'

def test_update_task(client):
    # Crear primero
    client.post('/tasks', json={'title': 'Actualizar'})
    resp = client.put('/tasks/1', json={'done': True})
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['done'] == True

def test_delete_task(client):
    client.post('/tasks', json={'title': 'Borrar'})
    resp = client.delete('/tasks/1')
    assert resp.status_code == 204
