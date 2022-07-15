from .extensions import db 


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(100))
    age = db.Column(db.Integer)
    password_digest = db.Column(db.String(10000))

    Preferences = db.Column(db.String(100))
    # (user_id)
    LikedBy = db.Column(db.String(100))
      # (user_id)
    Matches = db.Column(db.String(100))
      # (user_id)
    Events = db.Column(db.String(100))
    # (event_id)
    Rejected_Events = db.Column(db.String(100))

    rating = db.Column(db.String(100))
      #     Ratings - Array(Int)
    Chats = db.Column(db.String(100))
    # chat_id
  

    def __init__(self, name, email, age, password_digest, Preferences, LikedBy,  Matches, Events, Rejected_Events, rating, Chats):
        self.name = name
        self.email = email
        self.age = age
        self.password_digest = password_digest
        self.rating = rating
        self.Preferences = Preferences
        self.LikedBy = LikedBy 
        self.Matches = Matches
        self.Events = Events
        self.Rejected_Events = Rejected_Events
        self.Chats = Chats
    
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
            'Preferences': self.Preferences,
            'LikedBy': self.LikedBy,
            'Matches': self.Matches,
            'Events': self.Events,
            'Rejected_Events': self.Rejected_Events,
            'Chats': self.Chats
        }
