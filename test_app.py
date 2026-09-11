import pytest
from app import app, add

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """测试首页"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['app'] == 'CI/CD Demo'
    assert 'version' in data

def test_health(client):
    """测试健康检查"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_add():
    """测试业务逻辑"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
