from flask import Flask, current_app, request,Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from config import Config
from flask_migrate import Migrate
from app import auth , main

db = SQLAlchemy()
migrate = Migrate()


def create_app(config=Config):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config.from_object(os.environ['APP_SETTINGS'])
    db.init_app(app)
    migrate.init_app(app, db)
    from app import models


    app.register_blueprint(main.main_bp)

    app.register_blueprint(auth.auth_bp)


    return app
