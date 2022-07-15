from flask import Flask, Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug import exceptions
from app.models import   Users
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db

main = Blueprint('main', __name__) 
CORS(main)


# app = Flask(__name__)
# CORS(app)



@main.route("/")
def hello():
    return "Hello World!"


# login route
# @main.route("/auth/login")
# def login():
#     return "Hello from login!"


# registration route
# @main.route("/auth/register", methods = ['POST', "GET"])
# def register():
#     if request.method=="POST":
#         try:
#             req = request.get_json()
#             username = req['username']
#             password = req['password']
            
#             user = Users.query.filter_by(username=username).first()
#             if user!=None:
#                 return jsonify('Username already exists!'), 202
            
#             hash = generate_password_hash(password)
#             new_user = Users(
#                 name = req['name'],
#                 username = req['username'],
#                 email = req['email'], 
#                 password_digest = hash,
#             )
#             db.session.add(new_user)
#             db.session.commit()
#             return jsonify(f"New user was added!"), 201
        
        
#         except:
#             raise exceptions.InternalServerError()



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


# get chat 
@main.route('/chat', methods=['GET','POST'])
def getAllChats():
    return 'chats'

# get all events 
@main.route('/events', methods=['GET','POST', 'PATCH'])
def getAllEvents():
    return 'events'

# get  events by id
@main.route('/chat/<int:event_id>/')
def getEventsId():
    return 'events'




if __name__ == "__main__":
    app.run(debug=True)


