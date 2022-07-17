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
    return "<h1>Hello world</h1>"


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

    # if request.method == 'PATCH':
    #     try:
    #         req = request.get_json()
    #         updated_name = req['updated_name']
    #         updated_username = req['updated_username']
    #         updated_email = req['updated_email']
    #         updated_age= req['updated_age']
    #         updated_preferences= req['updated_preferences']
    #         updated_likedby= req['updated_likedby']
    #         updated_matches= req['updated_matches']
    #         updated_rejected_events= req['updated__rejected_events']
    #         db.session.query(Users).filter(Users.id == user_id).update({Users.name: updated_name, Users.username: updated_username, Users.email: updated_email, Users.age: updated_age, Users.preferences: updated_preferences, Users.likedby: updated_likedby, Users.matches: updated_matches, Users.rejected_events: updated_rejected_events })
    #         db.session.commit()
    #         return f"sucessfully updated!", 201
    #     except:
    #         raise exceptions.InternalServerError()

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
@main.route('/events', methods=['GET'])
def getAllEvents():
    allEvents = Events.query.all()
    return  jsonify([e.serialize() for e in allEvents])



# get  events by id
@main.route('/events/<int:event_id>/',  methods=['GET', 'DELETE'])
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


# @main.route('/users/<int:user_id>/location',  methods=['PATCH'])
# def updateLocation(user_id):
#     if request.method == 'PATCH':
#         try: 
#             req = request.get_json()
#             updated_longitude = req['updated_longitude']
#             updated_latitude = req['updated_latitude']
#             db.session.query(Users).filter(Users.id == user_id).update({Users.longitude: updated_longitude, Users.latitude: updated_latitude})
#             db.session.commit()
#             return f"Location sucessfully updated!", 201
#         except:
#             raise exceptions.InternalServerError()




@main.route('/users/<int:user_id>',  methods=['PATCH'])
def updateUser(user_id):
    #  return 'UPDATE'
    if request.method == 'PATCH':
        try: 
            req = request.get_json()
          
            updated_name = req['updated_name']
            updated_username = req['updated_username']
            updated_email = req['updated_email']
            updated_age= req['updated_age']
            updated_preferences= req['updated_preferences']
            updated_likedby= req['updated_likedby']
            updated_matches= req['updated_matches']
            updated_rejected_events= req['updated_rejected_events']
            db.session.query(Users).filter(Users.id == user_id).update({Users.name: updated_name, Users.username: updated_username, Users.email: updated_email, Users.age: updated_age, Users.preferences: updated_preferences, Users.likedby: updated_likedby, Users.matches: updated_matches, Users.rejected_events: updated_rejected_events })
            db.session.commit()
            return f"sucessfully updated!", 201
        except:
            raise exceptions.InternalServerError()






# get chat 
@main.route('/chat', methods=['GET','POST'])
def getAllChats():
    return 'chats'










@main.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404


@main.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400



@main.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500




if __name__ == "__main__":
    app.run(debug=True)


