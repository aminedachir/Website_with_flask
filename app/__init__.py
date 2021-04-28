from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "17@lames.com"
app.config.from_object('config')

from app import routes
