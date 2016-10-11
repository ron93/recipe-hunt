from flask import Flask,Blueprint,render_template

mod = Blueprint('home',__name__,url_prefix='/home')

@mod.route('/')
def home():
    message = "welcome home"

    return render_template('home/index.html',message=message)