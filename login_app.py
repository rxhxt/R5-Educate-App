from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_login import login_user
from datetime import datetime
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user, UserMixin
app=Flask(__name__)
app.config['SECRET_KEY']='12334566545443234323432'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'

db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

class RegistrationForm(FlaskForm):
    typeOfUser = SelectField('Choose type of User', choices = [('Student', 'Student'), 
      ('Teacher', 'Teacher')])
    name = StringField('Full Name',
                           validators=[DataRequired(), Length(min=2, max=100) ])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2)])
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

class User(db.Model,UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    typeOfUser=db.Column(db.String(10), nullable=False)
    name=db.Column(db.String(150), nullable=False)
    email=db.Column(db.String(120), nullable=False, unique=True)
    password=db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"

@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(user_id)
    except:
        return None

@app.route("/signup",methods=['POST','GET'])
@app.route("/", methods=['POST','GET'])
def signup():
    if current_user.is_authenticated:
        return redirect("login.html")
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(typeOfUser=form.typeOfUser.data, name=form.name.data, email=form.email.data, password=hashed_password)
        try:
            db.session.add(user)
            db.session.commit()
            flash(f'Account Created for {form.name.data}!, you can now login :)', category='success')
            return redirect(url_for('login'))
        except:
            flash(f'The user is already registered!! Try to login!!', category='danger')    
    return render_template('signup.html', form=form)

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect("tp.html")
    form=LoginForm()
    print("LOL")
    if form.validate_on_submit():
        print("QQQQ")
        print(form.email.data)
        print(form.password.data)
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page=request.args.get('next')
            flash(f'Hey {user.name}! Good to see you back ;)', category='success')
            if next_page:
                return redirect(next_page)
            else:
                print("Logged In")
                return redirect(url_for('dashboard'))    
        else:
            flash(f'Login Unsuccessful. Please check the email and/or Password', 'danger')  
              
    return render_template('login.html', form=form)

# @app.route("/", methods=['GET', 'POST'])
# def main():
#     res=request.get_json()
#     print(res)
#     if request.method=='POST':
#         if res["id"]==0:
#             typeOfUser=res["selectInput_d"]
#             name=res["nameInput_d"]
#             email=res["emailInput_d"]
#             password=res["passwordInput_d"]
#             hashed_password=bcrypt.generate_password_hash(password).decode('utf-8')
#             user=User(typeOfUser=typeOfUser, name=name, email=email, password=hashed_password)
#             try:
#                 db.session.add(user)
#                 db.session.commit()
#                 return redirect("dashboard.html")
#             except:
#                 flash(f'Looks like you alreay have an account! Try logging in!')
#                 return redirect("main.html")    
            
#         else:
#             print("Login")    
#     else:        
#         return render_template("main.html")
    
    


if __name__=="__main__":
    app.run(debug=True)    