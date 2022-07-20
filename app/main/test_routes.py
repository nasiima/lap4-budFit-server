import json
from unittest import mock


def test_home(api):
    """connects to root route"""
    app = api.get('/')
    assert app.status == '200 OK'
    assert app.get_data() ==  b'<h1>Hello world</h1>'


def test_get_allusers(api):
    app = api.get('/users')
    assert app.status == '200 OK'
    assert b'user_id' in app.get_data()


def test_get_allEvents(api):
    app = api.get('/events')
    assert app.status == '200 OK'
    assert b'event_id' in app.get_data()


def test_get_allMatches(api):
    app = api.get('/matches')
    assert app.status == '200 OK'
    assert b'event_id' in app.get_data()


def test_get_oneuser(api):
    app = api.get('/users/1')
    assert app.status == '200 OK'
    assert b'user_id' in app.get_data()


def test_get_oneevent(api):
    app = api.get('/events/1')
    assert app.status == '200 OK'
    assert b'event_id' in app.get_data()


def test_404(api):
    app = api.get('/kjnmo')
    assert app.status == '404 NOT FOUND'


def test_400(api):
    app = api.post('/auth/login')
    assert app.status == '400 BAD REQUEST'


# class TestAPICase():
#     def test_get_users(self, api):
#         res = api.get('/api/users/:1')
#         assert res.status == '200 OK'
#         assert len(res.json) == 2

#     def test_patch_user(self, api):
#         mock_data = json.dumps({'name': 'Molly'})
#         mock_headers = {'Content-Type': 'application/json'}
#         res = api.patch('/api/users/:1', data=mock_data, headers=mock_headers)
#         assert res.json['id'] == 2
#         assert res.json['name'] == 'Molly'

