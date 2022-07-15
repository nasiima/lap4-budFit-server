from flask import Flask, current_app


from .extensions import db
from .app import main

# def create_app(config_file='settings.py'):
#     app = Flask(__name__)
  
#     app.config.from_pyfile(config_file)

#     db.init_app(app)

#     # app.register_blueprint(app)

#     return app


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    # JWTManager(app)
    # login_manager = LoginManager()
    # login_manager.init_app(app)
    # login_manager.login_view = "login"
    app.config.from_pyfile(config_file)

    db.init_app(app)

    app.register_blueprint(main)

    return app
