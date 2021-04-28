from flask import render_template, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
def home():
    return "Welcome"

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/login')
    return render_template('signup.html', form = form)