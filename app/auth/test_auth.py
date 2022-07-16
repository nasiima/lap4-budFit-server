import json
from unittest import mock
import werkzeug.security as security


def test_login(api):
    user_data = json.dumps({'username': "tester",'password': 'test'})
    mock_headers = {'Content-Type': 'application/json'}
    app= api.post('/auth/login', data=user_data, headers=mock_headers)
    assert app.status == '200 OK'



def test_404(api):
    app = api.get('/kjnmo')
    assert app.status == '404 NOT FOUND'
