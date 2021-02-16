from app.auth import auth_bp 
from flask import render_template,flash, redirect, url_for
from app.auth.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('main_bp.index'))
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
        login_user(user,remember=form.remember_me.data)
        return redirect(url_for('main_bp.index'))
    return render_template('auth/login.html',title='Sign in',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main_bp.index'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    pass
