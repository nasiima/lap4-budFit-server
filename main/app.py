from flask import Flask, Blueprint
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

@main.route('/users', methods=['GET'])
def getAllUsers():
    allUsers = Users.query.all()
    return  jsonify([e.serialize() for e in allUsers])



if __name__ == "__main__":
    app.run(debug=True)


