from flask import Flask
from config import config
# import app and database connection
from .api import configure_api
from .db import db


def create_app(config_name):
    app = Flask('api-planets')

    app.config.from_object(config[config_name])

    # configuration MongoEngine
    db.init_app(app)

    # function configuration app
    configure_api(app)

    return app
