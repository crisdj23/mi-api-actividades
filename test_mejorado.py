import pytest
import json
from app_mejorada import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Test del endpoint principal"""
    resp = client.get('/')
    assert resp.status_code == 200
    data = resp.get_json()
    assert 'mensaje' in data
    assert 'endpoints' in data

def test_get_activities(client):
    """Test para obtener todas las actividades"""
    resp = client.get('/activities')
    assert resp.status_code == 200
    data = resp.get_json()
    assert 'total' in data
    assert 'actividades' in data
    assert isinstance(data['actividades'], list)

def test_create_activity(client):
    """Test para crear una nueva actividad"""
    new_activity = {
        'titulo': 'Actividad de prueba',
        'prioridad': 'alta'
    }
    resp = client.post('/activities', json=new_activity)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data['titulo'] == 'Actividad de prueba'
    assert data['prioridad'] == 'alta'

def test_get_single_activity(client):
    """Test para obtener una actividad específica"""
    resp = client.get('/activities/1')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['id'] == 1

def test_update_activity(client):
    """Test para actualizar una actividad"""
    update_data = {'completada': True, 'prioridad': 'baja'}
    resp = client.put('/activities/1', json=update_data)
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['completada'] == True
    assert data['prioridad'] == 'baja'

def test_delete_activity(client):
    """Test para eliminar una actividad"""
    resp = client.delete('/activities/2')
    assert resp.status_code == 200
    data = resp.get_json()
    assert 'mensaje' in data

def test_get_stats(client):
    """Test para obtener estadísticas"""
    resp = client.get('/stats')
    assert resp.status_code == 200
    data = resp.get_json()
    assert 'total_actividades' in data
    assert 'completadas' in data
    assert 'pendientes' in data

def test_activity_not_found(client):
    """Test para actividad no encontrada"""
    resp = client.get('/activities/999')
    assert resp.status_code == 404
    data = resp.get_json()
    assert 'error' in data
