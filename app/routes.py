from flask import render_template
from app import app

@app.route('/')
@app.route('/signup')
def index():
    return render_template('signup.html')