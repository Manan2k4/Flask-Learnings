import os
import tempfile
import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # Create a temporary file to isolate the database for each test
    db_fd, db_path = tempfile.mkstemp()

    # Create the app with common configuration
    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    # Create the database and load test data
    with app.app_context():
        init_db()
        
        # Insert test data directly
        db = get_db()
        db.execute(
            "INSERT INTO user (username, password) VALUES (?, ?)",
            ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f')
        )
        db.execute(
            "INSERT INTO user (username, password) VALUES (?, ?)",
            ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79')
        )
        db.execute(
            "INSERT INTO post (title, body, author_id, created) VALUES (?, ?, ?, ?)",
            ('test title', 'test\nbody', 1, '2018-01-01 00:00:00')
        )
        db.commit()

    yield app

    # Clean up
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    """A test client for the app."""
    # Enable session cookies for testing
    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()


class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password},
            follow_redirects=False
        )

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)