from flask import Flask, render_template
import admin,home
from app.home.controllers import mod
from app.admin.controllers import mod

app = Flask(__name__)


# home.add_route(app)
# admin.add_route(app)

# register
app.register_blueprint(home.controllers.mod)
app.register_blueprint(admin.controllers.mod)

