from flask import Flask, current_app, request,Blueprint, render_template
import os
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

migrate = Migrate()
login = LoginManager()
login.login_view = 'login'



def create_app(config=Config):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config.from_object(os.environ['APP_SETTINGS'])
    db.init_app(app)
    with app.app_context():
        db.create_all()
    migrate.init_app(app, db)
    login.init_app(app)

    # require login to view restricted resources



    from app import auth , main

    app.register_blueprint(main.main_bp)

    app.register_blueprint(auth.auth_bp)


    return app
from app import models
