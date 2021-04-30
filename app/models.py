from datetime import datetime
from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100), unique = True, index = True)
    lastname = db.Column(db.String(100), unique = True, index = True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(120))
    posts = db.relationship('Post',backref='author',lazy='dynamic')

    def __repr__(self):
        return f"<user {self.email}>"

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime,index = True, default = datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return f"<Post {self.body}>"