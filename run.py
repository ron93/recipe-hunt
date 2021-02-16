from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

import app

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



if __name__ == '__main__':
    app.run()
