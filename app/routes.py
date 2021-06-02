from flask import render_template
from app import app
from app.forms import LoginForm
from app.models import User

@app.route('/')
@app.route('/index')
def home():
    return '<h1>Hello,world</h1>' '''
    <a href='/signup'>Signup</a>
    '''

@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html", form = form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = LoginForm()
    return render_template('signup.html', title='Sign In', form = form)
