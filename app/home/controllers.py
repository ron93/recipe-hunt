from flask import Flask, Blueprint, render_template, current_app
from firebase import firebase
import pprint

mod = Blueprint('home', __name__, url_prefix='/home')


@mod.route('/')
def home():
    # message = "welcome home"
    #
    # firebase_base_url = current_app.config.get('FIREBASE_DB_CONN')
    # firebase_add_recipe = current_app.config.get('FIREBASE_ADD_RECIPE_NODE')
    # firebase_con = firebase.FirebaseApplication(firebase_base_url, None)
    #
    # # query the recipe
    # recipe = firebase_con.get("/recipe/mutura", None)
    #
    # print recipe


    return render_template('home/index.html')

@mod.route('/recipes')
def recipes():
    return render_template('home/recipes.html')

@mod.route('/featured')
def featured():
    return render_template('home/featured.html')

@mod.route('/videos')
def videos():
    return render_template('home/videos.html')

@mod.route('/about')
def about():
    return render_template('home/about.html')

@mod.route('/blog')
def blog():
    return render_template('home/blog.html')