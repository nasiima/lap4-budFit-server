import json
from unittest import mock
import werkzeug.security as security
import pytest


def test_register(api):
    new_user_data = json.dumps({'username': "tester", 'email': "test@email.com", 'password': 'test'})
    mock_headers = {'Content-Type': 'application/json'}
    app= api.post('/auth/register', data = new_user_data, headers=mock_headers)
    assert app.status == '201 CREATED'
    

