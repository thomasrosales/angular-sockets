from flask import Flask
from flask_bcrypt import Bcrypt
from os import path, environ
from app.config import config


# APPLICATION CONFIGURATION

bcrypt = Bcrypt()


def create_app(environment="development"):

    app = Flask(__name__, instance_relative_config=True)

    bcrypt.init_app(app)

    env = environ.get("FLASK_ENV", environment)

    app.config.from_object(config[env])

    # jwt = JWTManager(app)
    # jwt.init_app(app)

    # MODULES

    with app.app_context():
        from websocket.websocket import websocket

    # BLUEPRINT

    app.register_blueprint(websocket, url_prefix="/")

    # INIT DB WITH CONTEXT
    # with app.app_context():
    #     from app import database

    #     database.init_db()

    # from app.database import Session

    # @app.teardown_appcontext
    # def shutdown_session(exception=None):
    #     Session.remove()

    return app
