from flask import Flask, current_app, request
from flask_sqlalchemy import SQLAlchemy
import os
from config import Config
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(config=Config):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config.from_object(os.environ['APP_SETTINGS'])
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def hello():
        return "Hello World!"


    @app.route('/<name>')
    def hello_name(name):
        return "Hello {}!".format(name)

    return app
