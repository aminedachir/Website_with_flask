import os
class config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "17@lames.com"