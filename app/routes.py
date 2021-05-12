from flask import render_template, redirect
from flask import flash
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user,logout_user
from app.models import User
from flask_login import current_user, login_user
from app.models import User

@app.route('/')
@app.route('/index')
def home():
    return '<h1>Hello,world</h1>' '''
    <a href='/signup'>Signup</a>
    '''

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect('/index')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(firstname=form.firstname.data).first()
        login_user(user)
        return redirect('/index')
    return render_template('signup.html', title='Sign In', form=form)
