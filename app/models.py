from .extensions import db 
import jwt
import datetime
import os


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    dob = db.Column(db.Integer)
    password_digest = db.Column(db.String(10000))
    preferences =  db.Column(db.String(140))
    picture = db.Column(db.String(10000))

    def __init__(self, name, username, email, dob, password_digest, preferences, pic):
        self.name = name
        self.username = username
        self.email = email
        self.dob = dob
        self.password_digest = password_digest
        self.preferences = preferences
        self.picture = picture
    
    
    def __repr__(self):
        return '<id {}>'.format(self.user_id)
    
    def serialize(self):
        return {
            'user_id': self.user_id,
            'name': self.name, 
            'username': self.username, 
            'email': self.email,
            'dob': self.dob,
            'password_digest': self.password_digest,
            'preferences': self.preferences,
            'picture': self.picture
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
    title =  db.Column(db.String(140))
    activity = db.Column(db.String(64))
    descr = db.Column(db.String(100))
    location = db.Column(db.String(64))
    spaces = db.Column(db.Integer)
    time = db.Column(db.DateTime)

    def __init__(self, activity, descr, location, spaces, time ):
        self.activity = activity
        self.descr = descr
        self.location = location
        self.spaces = spaces 
        self.time = time

    
    def __repr__(self):
        return '<id {}>'.format(self.event_id)
    
    def serialize(self):
        return {
       'event_id': self.event_id,
       'activity': self.activity,
       'descr': self.descr,
       'location': self.location,
       'spaces': self.spaces,
       'time': self.time
        }




class Matches(db.Model):
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))


    def __init__(self, chat_id, messages):
        self.event_id = event_id
        self.user_id = user_id

    def __repr__(self):
        return '<id {}>'.format(self.chat_id)
    
    def serialize(self):
        return {
            'chat_id': self.event_id, 
            'messages': self.user_id
        }












# class Chats(db.Model):
#     chat_id = db.Column(db.Integer, primary_key=True)
#     messages = db.Column(db.Integer, db.ForeignKey('messages.message_id'))


#     def __init__(self, chat_id, messages):
#         self.chat_id = chat_id
#         self.messages = messages

#     def __repr__(self):
#         return '<id {}>'.format(self.chat_id)
    
#     def serialize(self):
#         return {
#             'chat_id': self.chat_id, 
#             'messages': self.messages
#         }




# class Messages(db.Model):
#     message_id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     comment = db.Column(db.String(140))
#     time = db.Column(db.DateTime, nullable=False)


#     def __init__(self, chat_id, messages):
#         self.message_id =  message_id
#         self.user_id = user_id
#         self.comment = comment
#         self.time = time

#     def __repr__(self):
#         return '<id {}>'.format(self.message_id)
    
#     def serialize(self):
#         return {
#             'message_id': self.message_id, 
#             'user_id': self.user_id,
#             'comment': self.comment,
#             'time': self.time
#         }

