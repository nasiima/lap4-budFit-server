

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
