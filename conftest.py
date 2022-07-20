from app.models import Events, Users, Matches
from app import create_app
import pytest

app = create_app()

@pytest.fixture
def api():
    client = app.test_client()
    return client

@pytest.fixture(scope='module')
def new_user():
    user = Users('patkennedy79@gmail.com', 'FlaskIsAwesome', '25.03.1988')
    return user


@pytest.fixture(scope='module')
def new_event():
    event = Events('football', 'casual', 'London')
    return event


@pytest.fixture(scope='module')
def new_Match():
    match = Matches('1', '2', '3')
    return match
