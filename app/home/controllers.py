from flask import Flask, Blueprint, request,session,render_template, url_for,current_app,redirect
from firebase import firebase
import pprint
from app.models import Base, engine,Recipe
from sqlalchemy.orm import sessionmaker
from forms import *

# Create session and connect to DB
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
db_session = DBSession()


mod = Blueprint('home', __name__, url_prefix='/home')


@mod.route('/')
def home():


    # firebase_base_url = current_app.config.get('FIREBASE_DB_CONN')
    # firebase_add_recipe = current_app.config.get('FIREBASE_ADD_RECIPE_NODE')
    # firebase_con = firebase.FirebaseApplication(firebase_base_url, None)
    #
    # # query the recipe
    # recipe = firebase_con.get("/recipe/mutura", None)
    #
    # print recipes



    return render_template('home/index.html', recipes=recipes)

@mod.route('/recipes')
def recipes():
    recipe =db_session.query(Recipe).all()
    print recipe


    return render_template('home/recipes.html' ,recipe=recipe)


@mod.route('/add' ,methods=["POST","GET"])

def add_recipe():


    if request.method == "POST":
        new_recipe = Recipe(name=request.form['name'], ingredients=request.form['ingredients'], steps=request.form['steps'])

        db_session.add(new_recipe)
        db_session.commit()

        return redirect(url_for('home.recipes'))

    else:
        return render_template('home/add.html')



#
#
# @mod.route('/add' ,methods=['POST','GET'])
#
# def add_recipe():
#     firebase_base_url = current_app.config.get('FIREBASE_DB_CONN')
#     firebase_add_recipe = current_app.config.get('FIREBASE_ADD_RECIPE_NODE')
#     firebase_con = firebase.FirebaseApplication (firebase_base_url, None)
#
#     form = add_recipe()
#     if request.method =='POST':
#
#
#         recipe = {'Name':form.name.data,'Ingredients':form.content.data,'Steps':form.steps.data}
#
#         firebase_con.put('/recipe', name=form.name.data.lower(), data=recipe)
#
#         return render_template('site/site.html' ,recipe=recipe)
#

