from .extensions import db 


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(100))
    age = db.Column(db.Integer)
    password_digest = db.Column(db.String(10000))

    # Preferences = db.Column(db.String(100))
    # # (user_id)
    # LikedBy = db.Column(db.String(100))
    #   # (user_id)
    # Matches = db.Column(db.String(100))
    #   # (user_id)
    # Events = db.Column(db.String(100))
    # # (event_id)
    # Rejected_Events = db.Column(db.String(100))

    # rating = db.Column(db.String(100))
    #   #     Ratings - Array(Int)
    # Chats = db.Column(db.String(100))
    # # chat_id
  

    def __init__(self, name, email, age, password_digest, Preferences, LikedBy,  Matches, Events, Rejected_Events, rating, Chats):
        self.name = name
        self.email = email
        self.age = age
        self.password_digest = password_digest
        self.rating = rating
        # self.Preferences = Preferences
        # self.LikedBy = LikedBy 
        # self.Matches = Matches
        # self.Events = Events
        # self.Rejected_Events = Rejected_Events
        # self.Chats = Chats
    
    def __repr__(self):
        return '<id {}>'.format(self.user_id)
    
    def serialize(self):
        return {
            'user_id': self.user_id,
            'name': self.name, 
            'email': self.email,
            'age': self.age,
            'password_digest': self.password_digest,
            'rating': self.rating,
            # 'Preferences': self.Preferences,
            # 'LikedBy': self.LikedBy,
            # 'Matches': self.Matches,
            # 'Events': self.Events,
            # 'Rejected_Events': self.Rejected_Events,
            # 'Chats': self.Chats
        }



class Events(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    activity = db.Column(db.String(64))
    desc = db.Column(db.String(100))
    location = db.Column(db.String(64))
    Spaces = db.Column(db.Integer)
    Age = db.Column(db.Integer)
    Pic = db.Column(db.String(64))
    SkillLevel = db.Column(db.String(64))
    Time = db.Column(db.String(64))
    LookingFor = db.Column(db.String(64))
    partysize = db.Column(db.String(64))



    def __init__(self,  user_id, activity, desc, location, Spaces, Age, Pic, SkillLevel, Time, LookingFor, partysize ):
        self.user_id = user_id
        self.activity = activity
        self.desc = desc
        self.location = location
        self.Spaces = Spaces 
        self.Age = Age
        self.Pic = Pic
        self.SkillLevel = SkillLevel
        self.Time = Time
        self.LookingFor = LookingFor
        self.partysize = partysize
    
    def __repr__(self):
        return '<id {}>'.format(self.event_id)
    
    def serialize(self):
        return {
       'user_id': self.user_id,
       'event_id': self.event_id,
       'activity': self.activity,
       'desc': self.desc,
       'location': self.location,
       'Spaces': self.Spaces,
       'Age': self.Age,
       'Pic': self.Pic,
       'SkillLevel': self.SkillLevel,
       'Time': self.Time,
       'LookingFor': self.LookingFor,
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

