from app.auth import auth_bp
from flask import render_template
from app.auth.forms import LoginForm

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('auth/login.html',title='Sign in',form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    pass
