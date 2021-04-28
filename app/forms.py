from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class loginform(FlaskForm):
    firstname = StringField("firstname", validators=[DataRequired()])
    lastname = StringField("lastname", validators=[DataRequired()])