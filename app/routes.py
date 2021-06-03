from flask import render_template, flash
from app import app
from app.forms import LoginForm
from app.models import User

@app.route('/')
@app.route('/index')
def home():
    return '<h1>Hello,world</h1>' '''
    <a href='/signup'>Signup</a>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("login.html", form = form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = LoginForm()
    if form.validate_on_submit():
        new_user = User(firstname = from.firstname.data, lastname = form.lastname.data \
            email = form.email.data)
        db.session.add(new_user)
        sb.session.commit()
        return "new user account created now !!"
    return render_template('signup.html', title='Sign In', form = form)
