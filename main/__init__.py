from flask import Flask, current_app


from .extensions import db
from .app import app

def create_app(config_file='settings.py'):
    app = Flask(__name__)
  
    app.config.from_pyfile(config_file)

    db.init_app(app)

    app.register_blueprint(app)

    return app