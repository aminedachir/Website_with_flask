from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100), unique = True, index = True)
    lastname = db.Column(db.String(100), unique = True, index = True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(120))
    posts = db.relationship('Post',backref='author',lazy='dynamic')

    def __repr__(self):
        return f"<User{self.firstname}>"