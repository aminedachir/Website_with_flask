from flask import render_template, redirect
from app import app
from app import db
from app.forms import LoginForm, LoginForm2
from app.models import User

@app.route('/')
@app.route('/index')
def home():
    return '<h1>Hello,world</h1>' '''
    <a href='/signup'>Signup</a>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm2()
    if form.validate_on_submit():
        return 'hello'
    return render_template("login.html", form = form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = LoginForm()
    if form.validate_on_submit():
        new_user = User(firstname = form.firstname.data, email = form.email.data, password = form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')
    return render_template('signup.html', title='Sign In', form = form)
