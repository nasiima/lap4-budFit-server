from flask import Flask, Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug import exceptions
from .models import   Users


main = Blueprint('main', __name__) 
CORS(main)


# app = Flask(__name__)
# CORS(app)



@main.route("/")
def hello():
    return "Hello World!"


# login route
@main.route("/auth/login")
def login():
    return "Hello from login!"


# registration route
@main.route("/auth/register")
def register():
    return "Hello from register!"



# get all users route
@main.route('/users', methods=['GET'])
def getAllUsers():
    allUsers = Users.query.all()
    return  jsonify([e.serialize() for e in allUsers])



# get  user by id
@main.get('/users/<int:user_id>/')
def getUserById():
    return 'user by id'


# get chat 
@main.route('/chat', methods=['GET','POST'])
def getAllChats():
    return 'chats'

# get all events 
@main.route('/events', methods=['GET','POST'])
def getAllEvents():
    return 'events'

# get all events 
@main.route('/chat/<int:event_id>/')
def getEventsId():
    return 'events'





if __name__ == "__main__":
    app.run(debug=True)


