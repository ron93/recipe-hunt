from app.auth import auth_bp 
from flask import render_template,flash, redirect, url_for,request
from app.auth.forms import LoginForm
from flask_login import current_user, login_user
from werkzeug.urls import url_parse
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
            
        login_user(user, remember=form.remember_me.data)

        #page redirect if login_required treiggered 
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

        return redirect(url_for('main_bp.index'))
    return render_template('auth/login.html',title='Sign in',form=form)

@app.route('/logout')
def logout():
    return redirect(url_for('main_bp.index'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    pass
