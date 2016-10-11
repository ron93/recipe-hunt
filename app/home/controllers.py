from flask import Flask, Blueprint, render_template, current_app
from firebase import firebase
import pprint

mod = Blueprint('home', __name__, url_prefix='/home')


@mod.route('/')
def home():
    # message = "welcome home"

    firebase_base_url = current_app.config.get('FIREBASE_DB_CONN')
    firebase_add_recipe = current_app.config.get('FIREBASE_ADD_RECIPE_NODE')
    firebase_con = firebase.FirebaseApplication(firebase_base_url, None)

    # query the recipe
    recipe = firebase_con.get("/recipe/mutura", None)

    print recipe


    return render_template('home/index.html', recipe=recipe)
