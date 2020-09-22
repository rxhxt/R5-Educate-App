from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from login_app import User



class RegistrationForm(FlaskForm):
    typeOfUser = SelectField('Choose type of User', choices = [('Student', 'Student'), 
      ('Teacher', 'Teacher')])
    name = StringField('Full Name',
                           validators=[DataRequired(), Length(min=2, max=100) ])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit=SubmitField('Sign Up Now')

    def validate_email(self, email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('The email is already taken! Please choose a different one!')    



class LoginForm(FlaskForm):
    email=StringField('Email', validators=[DataRequired(),Email()]) 
    password = PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField('Login')