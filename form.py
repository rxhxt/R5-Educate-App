from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Full Name', validators=[DataRequired()])
    emailaddress= StringField('Email Adress', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    passwordConf = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('SignUp Now')