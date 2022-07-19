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


# get all users route
@cross_origin()
@main.route('/users', methods=['GET'])
def getAllUsers():
    allUsers = Users.query.all()
    return  jsonify([e.serialize() for e in allUsers])

# @main.route('/users', methods=['GET'])
# def getAllUsers():
#     allUsers = Users.query.all()
#     return  jsonify([e.serialize() for e in allUsers])
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response


# get  user by id and delete user by id

@cross_origin()
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



# get all events 
@cross_origin()
@main.route('/events', methods=['GET'])
def getAllEvents():
    allEvents = Events.query.all()
    return  jsonify([e.serialize() for e in allEvents])

    # elif request.method == 'POST':
    #     try:
    #         req = request.get_json()
    #         new_event = Products(
    #             # user_id = req['user_id'],
    #             activity = req['activity'], 
    #             title = req['title'],
    #             descr = req['descr'], 
    #             location = req['location'],
    #             spaces = req['spaces'],  
    #             date = req['date']
    #         )
    #         db.session.add(new_event)
    #         db.session.commit()
    #         return f"New Event was added!", 201

    #     except: 
    #         raise exceptions.InternalServerError()




# get  events by id and delete event by id
@cross_origin()
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





#  get matches by id and delete match by id
@cross_origin()
@main.route('/matches/<int:match_id>/',methods=['GET', 'DELETE'])
def getMatchesById(match_id):
     if request.method == 'GET':
        try: 
            match = Matches.query.get_or_404(match_id)
            return  jsonify([match.serialize()])
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








@main.route('/users/<int:user_id>',  methods=['PATCH'])
def updateUser(user_id):
    if request.method == 'PATCH':
        try: 
            req = request.get_json()
            print(req)
          
            updated_name = req['updated_name']
            updated_username = req['updated_username']
            updated_email = req['updated_email']
            updated_dob = req['updated_dob']
            updated_preferences = req['updated_preferences']
            updated_picture = req['updated_picture']
            db.session.query(Users).filter(Users.id == user_id).update({Users.name: updated_name, Users.username: updated_username, Users.email: updated_email, Users.dob: updated_dob, Users.preferences: updated_preferences, Users.picture: updated_picture })
            db.session.commit()
            return f"sucessfully updated!", 201
        except:
            raise exceptions.InternalServerError()


@main.route('/events/<int:event_id>',  methods=['PATCH'])
def updateEvent(event_id):
    if request.method == 'PATCH':
        try: 
            req = request.get_json()
            print(req)
            updated_title = req['updated_title']
            updated_activity = req['updated_activity']
            updated_descr = req['updated_descr']
            updated_location = req['updated_location']
            updated_spaces= req['updated_spaces']
            updated_date = req['updated_date']
            db.session.query(Events).filter(Events.id == event_id).update({Events.title: updated_title, Events.activity: updated_activity, Events.descr: updated_descr, Events.location: updated_location, Events.spaces: updated_spaces, Events.date: updated_date })
            db.session.commit()
            return f"sucessfully updated!", 201
        except:
            raise exceptions.InternalServerError()


#  get all matches
@cross_origin()
@main.route('/matches', methods=['GET'])
def getAllMatches():
    allMatches = Matches.query.all()
    return  jsonify([e.serialize() for e in allMatches])

# get chat 
# @main.route('/chat', methods=['GET','POST'])
# def getAllChats():
#     return 'chats'










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


