from .extensions import db 


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

