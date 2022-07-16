from flask import Flask, Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug import exceptions
from app.models import   Users, Events
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db

main = Blueprint('main', __name__) 
CORS(main)


@main.route("/")
def hello():
    return "Hello World!"


# get all users route
@main.route('/users', methods=['GET'])
def getAllUsers():
    allUsers = Users.query.all()
    return  jsonify([e.serialize() for e in allUsers])



# get  user by id
@main.route('/users/<int:user_id>/', methods=['GET', 'DELETE', 'PATCH'])
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


# get all events 
@main.route('/events', methods=['GET','POST', 'PATCH'])
def getAllEvents():
    allEvents = Events.query.all()
    return  jsonify([e.serialize() for e in allEvents])




# get chat 
@main.route('/chat', methods=['GET','POST'])
def getAllChats():
    return 'chats'


# get  events by id
@main.route('/chat/<int:chat_id>/')
def getEventsId():
    return 'events'




if __name__ == "__main__":
    app.run(debug=True)


