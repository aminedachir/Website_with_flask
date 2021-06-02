from flask import Flask
from flask_login import LoginManager
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
login = LoginManager(app)
app.config['SECRET_KEY'] = "Admemdcin31431@adm"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/amine/new_website/src/app.db'
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

