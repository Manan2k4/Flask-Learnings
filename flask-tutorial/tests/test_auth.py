import pytest
from flask import g, session
from flaskr.db import get_db

def test_register(client, app):
    assert client.get('/auth/register').status_code == 200
    response = client.post (
        '/auth/register', data={'username': 'a', 'password': 'a'}
    )
    assert response.headers["Location"] == "/auth/login"

    with app.app_context():
        assert get_db().execute(
            "select * from user where username = 'a'",
        ).fetchone() is not None

@pytest.mark.parametrize(('username', 'password', 'message'),(
    ('', '', b'Username is required.'),
    ('a', '', b'Password is required'),
    ('test', 'test', b'already registered'),
))
def test_register_validate_input(client, username, password, message):
    response = client.post(
        '/auth/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data

def test_login(client, auth):
    assert client.get('/auth/login').status_code == 200
    response = auth.login()
    assert response.headers["Location"] == "/"

@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('a', 'test', b'Incorrect Username.'),
    ('test', 'a', b'Incorrect Password.'),
))
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data

def test_logout(client, auth):
    auth.login()
    auth.logout()
    assert 'user_id' not in session

def test_debug_login(client, auth):
    response = auth.login()
    print(f"Status: {response.status_code}")
    print(f"Headers: {response.headers}")
    print(f"Data: {response.data}")