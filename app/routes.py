from flask import render_template, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form = form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/login')
    return render_template('signup.html', form = form)