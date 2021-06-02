import os
basedir = os.path.abspath(os.path.dirname(__file__))
class config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "17@lames.com"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///home/amine/new_website/src/app.db' + os.path.join(basedir, 'app.db')