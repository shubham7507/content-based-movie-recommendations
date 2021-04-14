from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class SignUpForm(FlaskForm):
    moviename = StringField('Enter Moviename')
    submit = SubmitField('submit')
