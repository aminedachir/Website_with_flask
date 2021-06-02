from flask import render_template, redirect, flash
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user,logout_user
from app.models import User

@app.route('/')
@app.route('/index')
def home():
    return '<h1>Hello,world</h1>' '''
    <a href='/signup'>Signup</a>
    '''

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = LoginForm()
    if form.validate_on_submit():
        flash("registred !!")
    return render_template('signup.html', title='Sign In', form=form)
