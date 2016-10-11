from flask import Flask,Blueprint,render_template

# def blueprint
mod = Blueprint('site',__name__,url_prefix='/recipe')

@mod.route('/')
def site():

    return render_template('site/site.html')

