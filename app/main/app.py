from flask import Flask, Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug import exceptions
from app.models import   Users, Events
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


# get  events by id
@main.route('/events/<int:event_id>/',  methods=['GET', 'DELETE', 'PATCH'])
def getEventsId(event_id):
    if request.method == 'GET':
        try: 
            event = Events.query.get_or_404(event_id)
            return  jsonify([event.serialize()])
        except exceptions.NotFound:
            raise exceptions.NotFound("Event not found!")
        except:
            raise exceptions.InternalServerError()
    elif request.method == 'DELETE':
        try: 
            event = Events.query.get_or_404(event_id)
            db.session.delete(event)
            db.session.commit()
            return f"Event was sucessfully deleted!", 204
        except exceptions.NotFound:
            raise exceptions.NotFound("Event not found!")
        except:
            raise exceptions.InternalServerError()
    


# get chat 
@main.route('/chat', methods=['GET','POST'])
def getAllChats():
    return 'chats'





if __name__ == "__main__":
    app.run(debug=True)


