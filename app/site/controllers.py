from flask import Flask,Blueprint,render_template,current_app,request
from firebase import firebase
from .forms import add_recipe

# def blueprint
mod = Blueprint('site',__name__,url_prefix='/recipe')

@mod.route('/')
def site():

    return render_template('site/site.html')


@mod.route('/add' ,methods=['POST','GET'])

def add_recipe():
    firebase_base_url = current_app.config.get('FIREBASE_DB_CONN')
    firebase_add_recipe = current_app.config.get('FIREBASE_ADD_RECIPE_NODE')
    firebase_con = firebase.FirebaseApplication (firebase_base_url, None)

    form = add_recipe()
    if request.method =='POST':


        recipe = {'Name':form.name.data,'Ingredients':form.content.data,'Steps':form.steps.data}

        firebase_con.put('/recipe', name=form.name.data.lower(), data=recipe)

        return render_template('site/site.html' ,recipe=recipe)


