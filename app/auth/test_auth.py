from flask import session, request
import json
from unittest import mock
import werkzeug.security as security


def test_login(api):
    user_data = json.dumps({'username': "tester",'password': 'test'})
    mock_headers = {'Content-Type': 'application/json'}
    app= api.post('/auth/login', data=user_data, headers=mock_headers)
    # assert app.status == '200 OK'

def test_register(api):
    user_data = json.dumps({'username': "tester", 'password': 'test'})
    mock_headers = {'Content-Type': 'application/json'}
    app = api.post('/auth/register', data=user_data, headers=mock_headers)


def test_400(api):
    app = api.post('/auth/login')
    assert app.status == '400 BAD REQUEST'


def test_401(api):
    app = api.post('/auth/login')
    user_data = json.dumps({'username': "tester", 'password': ''})
    mock_headers = {'Content-Type': 'application/json'}
    app = api.post('/auth/login', data=user_data, headers=mock_headers)
    # assert app.status == '401 UNAUTHORIZED'


def test_404(api):
    app = api.get('/kjnmo')
    assert app.status == '404 NOT FOUND'






