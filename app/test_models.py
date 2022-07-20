from app.models import Users, Events, Matches


def test_new_user_with_fixture():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, password_digest, and name fields are defined correctly
    """
    user = Users('George', 'gman', 'gmiller04@yaho.com', '25.03.1988', 'password', 'football', 'image')
    assert user.name == 'George'
    assert user.username == 'gman'
    assert user.email == 'gmiller04@yaho.com'
    assert user.dob == '25.03.1988'
    assert user.password_digest == 'password'
    assert user.preferences == 'football'
    assert user.picture == 'image'

def test_new_event_with_fixture():
    """
    GIVEN a Events model
    WHEN a new Event is created
    THEN check the name, description, and location fields are defined correctly
    """
    event = Events('football', 'football', 'casual', 'London', '5', 'today' )
    assert event.title == 'football'
    assert event.activity == 'football'
    assert event.descr == 'casual'
    assert event.location == 'London'
    assert event.spaces == '5'
    assert event.date == 'today'


def test_new_match_with_fixture():
    """
    GIVEN a Match model
    WHEN a new Match is created
    THEN check the match, event, and user id are defined correctly
    """

    match = Matches('1','2','3')
    assert match.match_id == '1'
    assert match.event_id == '2'
    assert match.user_id == '3'
