from flask import render_template, redirect, flash,url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user,logout_user
from app.models import User
from flask_login import current_user, login_user
from app.models import User

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(firstname=form.firstname.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('index'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
