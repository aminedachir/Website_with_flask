from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = "17@lames.com"
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(db,app)

from app import routes

