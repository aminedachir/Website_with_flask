from flask import render_template, redirect
from flask.helpers import flash
from flask_login import current_user, login_user, logout_user
from app import app
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.forms import LoginForm, LoginForm2
from app.models import User

@app.route('/')
@app.route('/index')
def home():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/index')
    form = LoginForm2()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password,form.password.data):
                return redirect('/index')
        return "INVALID"
    return render_template('login.html', title='Sign In', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = LoginForm()
    if form.validate_on_submit():
        if form.firstname.data == form.password.data:
            return "Don't write your name in your password"
        else:
            new_user = User(firstname = form.firstname.data, email = form.email.data, password = generate_password_hash(form.password.data))
            db.session.add(new_user)
            db.session.commit()
            return redirect('/login')
    return render_template('signup.html', title='Sign In', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')
