import pytest
from main import *


@pytest.fixture
def client():
    """Configures the app for testing

    Sets app config variable ``TESTING`` to ``True``

    :return: App for testing
    """

    # app.config['TESTING'] = True
    client = app.test_client()

    yield client


def test_landing(client):
    landing = client.get("/")
    html = landing.data.decode()

    assert "Select The State You Live In" in html
    assert landing.status_code == 200


def test_file_display(client):
    aws_files = client.get('/files')
    html = aws_files.data.decode()

    assert "Click on the filename to download it" in html
    assert aws_files.status_code == 200
