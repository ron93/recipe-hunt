from flask import Flask, render_template,app
import admin,home


from app.home.controllers import mod
from app.admin.controllers import mod
from app.site.controllers import mod

app = Flask(__name__)
# configurations
app.config.from_object('config')




# register blueprints

# home page blueprint
app.register_blueprint(home.controllers.mod)

# admin blueprint
app.register_blueprint(admin.controllers.mod)

# site blueprint
app.register_blueprint(site.controllers.mod)

