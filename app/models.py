from .extensions import db 
import jwt
import datetime


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    age = db.Column(db.Integer)
    password_digest = db.Column(db.String(10000))
    preferences = db.Column(db.String(100))
    # # (user_id)
    likedby = db.Column(db.String(100))
    #   # (user_id)
    matches = db.Column(db.String(100))
    #   # (user_id)
    events = db.Column(db.String(100))
    # # (event_id)
    rejected_events = db.Column(db.String(100))
    rating = db.Column(db.String(100))
    #   #     Ratings - Array(Int)
    chats = db.Column(db.String(100))
    # # chat_id
  

    def __init__(self, name, username, email, age, password_digest, preferences, likedby,  matches, events, rejected_events, rating, chats):
        self.name = name
        self.username = username
        self.email = email
        self.age = age
        self.password_digest = password_digest
        self.rating = rating
        self.preferences = preferences
        self.likedby = likedby 
        self.matches = matches
        self.events = events
        self.rejected_events = rejected_events
        self.chats = chats
    
    def __repr__(self):
        return '<id {}>'.format(self.user_id)
    
    def serialize(self):
        return {
            'user_id': self.user_id,
            'name': self.name, 
            'username': self.username, 
            'email': self.email,
            'age': self.age,
            'password_digest': self.password_digest,
            'rating': self.rating,
            'preferences': self.preferences,
            'likedby': self.likedby,
            'matches': self.matches,
            'events': self.events,
            'rejected_events': self.rejected_events,
            'chats': self.chats
        }
        
    def encode_auth_token(self, username):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                'iat': datetime.datetime.utcnow(),
                'sub': username
            }
            return jwt.encode(
                payload,
                os.environ.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, os.environ.get('SECRET_KEY'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'



class Events(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    activity = db.Column(db.String(64))
    descr = db.Column(db.String(100))
    location = db.Column(db.String(64))
    spaces = db.Column(db.Integer)
    age = db.Column(db.Integer)
    pic = db.Column(db.String(64))
    skilllevel = db.Column(db.String(64))
    time = db.Column(db.String(64))
    lookingfor = db.Column(db.String(64))
    partysize = db.Column(db.String(64))

    # def __init__(self,  user_id, activity, descr, location, spaces, age, pic, skilllevel, time, lookingfor, partysize ):
    def __init__(self, activity, descr, location, spaces, age, pic, skilllevel, time, lookingfor, partysize ):
        # self.user_id = user_id
        self.activity = activity
        self.descr = descr
        self.location = location
        self.spaces = spaces 
        self.age = age
        self.pic = pic
        self.skilllevel = skilllevel
        self.time = time
        self.lookingfor = lookingfor
        self.partysize = partysize
    
    def __repr__(self):
        return '<id {}>'.format(self.event_id)
    
    def serialize(self):
        return {
    #    'user_id': self.user_id,
       'event_id': self.event_id,
       'activity': self.activity,
       'descr': self.descr,
       'location': self.location,
       'spaces': self.spaces,
       'age': self.age,
       'pic': self.pic,
       'skilllevel': self.skilllevel,
       'time': self.time,
       'lookingfor': self.lookingfor,
       'partysize': self.partysize 
        }





class Chat(db.Model):
    chat_id = db.Column(db.Integer, primary_key=True)
    messages = db.Column(db.Integer, db.ForeignKey('message.id'))


    def __init__(self, chat_id, messages):
        self.chat_id = chat_id
        self.messages = messages

    def __repr__(self):
        return '<id {}>'.format(self.chat_id)
    
    def serialize(self):
        return {
            'chat_id': self.chat_id, 
            'messages': self.messages
        }

