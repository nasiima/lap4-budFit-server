from flask import Flask, Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug import exceptions
from .models import   Users
from werkzeug.security import generate_password_hash, check_password_hash


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
@main.route('/users/<int:user_id>/', methods=['GET', 'DELETE'])
def getUserById(user_id):
    if request.method == 'GET':
        try: 
            user = Users.query.get_or_404(user_id)
            return  jsonify([user.serialize()])
        except exceptions.NotFound:
            raise exceptions.NotFound("User not found!")
        except:
            raise exceptions.InternalServerError()
    elif request.method == 'DELETE':
        try: 
            user = Users.query.get_or_404(user_id)
            
            db.session.delete(user)
            db.session.commit()
            return f"User was sucessfully deleted!", 204
        except exceptions.NotFound:
            raise exceptions.NotFound("User not found!")
        except:
            raise exceptions.InternalServerError()
    # return 'user by id'


# get chat 
@main.route('/chat', methods=['GET','POST'])
def getAllChats():
    return 'chats'

# get all events 
@main.route('/events', methods=['GET','POST'])
def getAllEvents():
    return 'events'

# get  events by id
@main.route('/chat/<int:event_id>/')
def getEventsId():
    return 'events'




if __name__ == "__main__":
    app.run(debug=True)


