
from app import create_app
import pytest

app = create_app()

@pytest.fixture
def api():
    client = app.test_client()
    return client

