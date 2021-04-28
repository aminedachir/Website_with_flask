from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
def home():
    return "Welcome"
@app.route('/signup')
def signup():
    form = LoginForm()
    return render_template('signup.html', form = form)