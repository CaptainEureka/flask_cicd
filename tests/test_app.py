import pytest
from website import create_app

test_names = ['Max', 'Emi', 'Muffin']

@pytest.fixture(scope = 'module')
def test_client():
    flask_app = create_app()

    with flask_app.test_client() as testing_client:
        yield testing_client

def test_get_welcome_page(test_client):
    response = test_client.get('/welcome')
    assert response.status_code == 200

def test_get_welcome_named(test_client):
    for name in test_names:
        response = test_client.get(f'/welcome/{name}')
        assert str.encode(name) in response.data

def test_get_index_hello(test_client):
    response = test_client.get('/')
    assert response.status_code == 200