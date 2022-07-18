
from flask import Flask, current_app

from .extensions import db
from .main.app import main
from .auth.auth import auth
# from .chat.app import chat




def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)
    # app.register_blueprint(chat)
    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app

