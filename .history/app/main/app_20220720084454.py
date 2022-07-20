from flask import Flask, Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from werkzeug import exceptions
from app.models import   Users, Events, Matches
from app.extensions import db

main = Blueprint('main', __name__) 
CORS(main)


@main.route("/")
def hello():
    return "<h1>Hello world</h1>"



@main.route('/users', methods=['GET'])
def getAllUsers():
    allUsers = Users.query.all()
    return  jsonify([e.serialize() for e in allUsers])
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# get  user by id and delete user by id

@cross_origin()
@main.route('/users/<int:user_id>/', methods=['GET', 'DELETE', 'PATCH'])
def getUserById(user_id):
    if request.method == 'GET':
        try: 
            user = Users.query.get_or_404(user_id)
            return  jsonify([user.serialize()])
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        except exceptions.NotFound:
            raise exceptions.NotFound("User not found!")
        except:
            raise exceptions.InternalServerError()

    if request.method == 'PATCH':
        try:           
            updated_name = request.json['name']
            updated_username = request.json['username']
            updated_email = request.json['email']
            updated_dob = request.json['dob']
            updated_preferences = request.json['preferences']
            updated_picture = request.json['picture']

            thisUser = Users.query.get(user_id)

            thisUser.name = updated_name
            thisUser.username = updated_username
            thisUser.email = updated_email
            thisUser.dob = updated_dob
            thisUser.preferences = updated_preferences
            thisUser.picture = updated_picture
            
            db.session.add(thisUser)
            db.session.commit()
            return f"sucessfully updated!", 201
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Methods', 'PATCH')
            return response
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



#  get by username
@cross_origin()
@main.route('/users/<username>/', methods=['GET'])
def getUserByUsername(username):
     if request.method == 'GET':
        try: 
            user = Users.query.filter_by(username=username).first()
            return  jsonify([user.serialize()])
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        except exceptions.NotFound:
            raise exceptions.NotFound("User not found!")
        except:
            raise exceptions.InternalServerError()



@cross_origin()
@main.route('/events', methods=['GET'])
def getAllEvents():
    allEvents = Events.query.all()
    return  jsonify([e.serialize() for e in allEvents])
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# get  events by id and delete event by id
@cross_origin()
@main.route('/events/<int:event_id>/',  methods=['GET', 'DELETE', 'PATCH'])
def getEventsId(event_id):
    if request.method == 'GET':
        try: 
            event = Events.query.get_or_404(event_id)
            return  jsonify([event.serialize()])
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        except exceptions.NotFound:
            raise exceptions.NotFound("Event not found!")
        except:
            raise exceptions.InternalServerError()
    if request.method == 'PATCH':
        try: 
            updated_title = request.json['title']
            updated_activity = request.json['activity']
            updated_descr = request.json['descr']
            updated_location = request.json['location']
            updated_spaces= request.json['spaces']
            updated_date = request.json['date']

            event = Events.query.get(event_id)
            
            event.title = updated_title
            event.activity = updated_activity
            event.descr = updated_descr
            event.location = updated_location
            event.spaces = updated_spaces
            event.date = updated_date

            db.session.add(event)
            db.session.commit()
            return f"sucessfully updated!", 201
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Methods', 'PATCH')
            return response
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



@cross_origin()
@main.route('/matches/<int:match_id>/',methods=['GET', 'DELETE'])
def getMatchesById(match_id):
     if request.method == 'GET':
        try: 
            match = Matches.query.get_or_404(match_id)
            return  jsonify([match.serialize()])
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        except exceptions.NotFound:
            raise exceptions.NotFound("Match not found!")
        except:
            raise exceptions.InternalServerError()
    
     elif request.method == 'DELETE':
        try: 
            match = Matches.query.get_or_404(match_id)
            db.session.delete(match)
            db.session.commit()
            return f"Event was sucessfully deleted!", 204
        except exceptions.NotFound:
            raise exceptions.NotFound("Event not found!")
        except:
            raise exceptions.InternalServerError()



# @cross_origin()
# @main.route('/users/<int:user_id>',  methods=['PATCH'])
# def updateUser(user_id):
#     if request.method == 'PATCH':
#         try:           
#             updated_name = request.json['name']
#             updated_username = request.json['username']
#             updated_email = request.json['email']
#             updated_dob = request.json['dob']
#             updated_preferences = request.json['preferences']
#             updated_picture = request.json['picture']

#             thisUser = Users.query.get(user_id)

#             thisUser.name = updated_name
#             thisUser.username = updated_username
#             thisUser.email = updated_email
#             thisUser.dob = updated_dob
#             thisUser.preferences = updated_preferences
#             thisUser.picture = updated_picture
            
#             db.session.add(thisUser)
#             db.session.commit()
#             return f"sucessfully updated!", 201
#             response.headers.add('Access-Control-Allow-Origin', '*')
#             response.headers.add('Access-Control-Allow-Methods', 'PATCH')
#             return response
#         except:
#             raise exceptions.InternalServerError()



# @cross_origin()
# @main.route('/events/<int:event_id>',  methods=['PATCH'])
# def updateEvent(event_id):
#     if request.method == 'PATCH':
#         try: 
#             updated_title = request.json['title']
#             updated_activity = request.json['activity']
#             updated_descr = request.json['descr']
#             updated_location = request.json['location']
#             updated_spaces= request.json['spaces']
#             updated_date = request.json['date']

#             event = Events.query.get(event_id)
            
#             event.title = updated_title
#             event.activity = updated_activity
#             event.descr = updated_descr
#             event.location = updated_location
#             event.spaces = updated_spaces
#             event.date = updated_date

#             db.session.add(event)
#             db.session.commit()
#             return f"sucessfully updated!", 201
#             response.headers.add('Access-Control-Allow-Origin', '*')
#             response.headers.add('Access-Control-Allow-Methods', 'PATCH')
#             return response

#         except:
#             raise exceptions.InternalServerError()



# #  get all matches
@cross_origin()
@main.route('/matches', methods=['GET'])
def getAllMatches():
    allMatches = Matches.query.all()
    return  jsonify([e.serialize() for e in allMatches])
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response




# # get chat 
# # @main.route('/chat', methods=['GET','POST'])
# # def getAllChats():
# #     return 'chats'






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


