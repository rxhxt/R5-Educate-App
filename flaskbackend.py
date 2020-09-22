from flask import render_template, request, flash, redirect, url_for
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_login import login_user,  current_user, logout_user, login_required
from datetime import datetime
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user, UserMixin
from flask import Flask, Response,redirect, url_for, request
import flask
# import summarize2.views as sv
from imports import *
from preprocess import *
from mail import *
import _sqlite3
from display_questions import StoreQuestions
import os
from flask import Flask,render_template,url_for,request,jsonify,make_response,redirect
from flask_mysqldb import MySQL
import form
from werkzeug.exceptions import BadRequestKeyError
import yaml
from hello import app2 as app2
from form import LoginForm
app = Flask(__name__, template_folder="templates",static_folder="static")
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'
app.config["PDF_UPLOADS"] = "static/pdf/uploads"
app.config["ALLOWED_EXTENSIONS"] = ["PDF"]
app.config["MAX_CONTENT_LENGTH"] = 20 * 1024 * 1024
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'
# {% comment %} <form class="form-inline" action="http://localhost:5000/q={{ q_id }}" method="post"> {% endcomment %}
# db=yaml.load(open('db.yaml'))
# app.config['MYSQL_HOST']=db['mysql_host']
# app.config['MYSQL_USER']=db['mysql_user']
# app.config['MYSQL_PASSWORD']=db['mysql_password']
# app.config['MYSQL_DB']=db['mysql_db']

mysql=MySQL(app)
name =""
acc_holder = ""
test_dict = {}

####################################Helper functions################################################

def check_answer(data):
    global test_dict
    store = StoreQuestions() 
    print(test_dict)
    print("-------------------")
    ans_dict = {"A":1,"B":2,"C":3,"D":4}
    for key in  test_dict.keys(): 
        if(test_dict.get(key)==ans_dict.get(data.iloc[key,6])):
            store.store_results(True,key)
        else:
            store.store_results(False,key)




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


@app.route("/student")
@login_required
def student():
    print(current_user.name)
    return render_template("layout_student.html", current_user=current_user)

@app.route("/signup",methods=['POST','GET'])
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
        print(user)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page=request.args.get('next')
            flash(f'Hey {user.name}! Good to see you back ;)', category='success')
            if next_page:
                return redirect(next_page)
            else:
                print("Logged In")
                return redirect(url_for('student'))    
        else:
            flash(f'Login Unsuccessful. Please check the email and/or Password', 'danger')  
              
    return render_template('login.html', form=form)

@app.route('/tests')
def testCover():
    return render_template('testcover.html')



@app.route('/q=<int:q_id>',methods = ['POST', 'GET'])
def test_page2(q_id):
   store = StoreQuestions() 
   data = store.get_questions(31)
   ans_dict = {"A":1,"B":2,"C":3,"D":4}
   global test_dict
   q_id = q_id-1
   if request.method == 'POST':
        try:
            user = request.form["SAE"]
            test_dict[q_id] = ans_dict.get(data.iloc[q_id,6])
            q_id=q_id+2
            return redirect(url_for('test_page2',q_id = q_id))
        except BadRequestKeyError as bk:
            print("oops")
        try: 
            temp = request.form['back-button']
            # q_id=q_id-1
            return redirect(url_for('test_page2',q_id = q_id))
        except BadRequestKeyError as bk:
            print("oops2")
        try: 
            temp = request.form['submit-button']
            check_answer(data
            )
            return  redirect(url_for('submission'))
        except BadRequestKeyError as bk:
            print("oops2")

   return flask.render_template('give_test.html', q_id = data['q_id'].unique()[q_id],
                                question = data['question'].unique()[q_id],
                                option_A = data['option_A'].unique()[q_id],
                                option_B = data['option_B'].unique()[q_id],
                                option_C = data['option_C'].unique()[q_id],
                                option_D = data['option_D'].unique()[q_id],)





def allowed_pdf(filename):
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    if ext.upper() in app.config["ALLOWED_EXTENSIONS"]:
        return True
    return False

@app.route('/upload-pdf', methods=["GET", "POST"])
def upload_pdf():
    if request.method == "POST":
        if request.files:
            pdf = request.files["pdf"]
            mail = request.form['email']

            if pdf.filename == "":
                return render_template('upload_pdf.html')
            if not allowed_pdf(pdf.filename):
                return render_template('upload_pdf.html')
            else:
                filename = 'pdf_file.pdf'
                pdf.save(os.path.join(app.config["PDF_UPLOADS"], filename))
                thread = Thread(target = pdfParser, kwargs={'filename': os.path.join(app.config["PDF_UPLOADS"], 'pdf_file.pdf'), 'mailid': f'{mail}'})
                thread.start()
                return render_template('upload_pdf.html')
        return redirect(request.url)
    return render_template('upload_pdf.html')



@app.route("/dashboard_teacher")
def dash_teacher():
    return render_template('dashboard.html')


@app.route("/dashboard_student")
def dash_stu():
    return render_template('dashboard_students.html')


@app.route('/submitted',methods = ['POST', 'GET'])
def submission():
    if request.method == 'POST':
        return redirect(url_for('hello_world'))
    global name
    return flask.render_template('success.html',name = name)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('signup'))


@app.route('/success')
def first():
    return redirect(url_for('my_dash_app')) 

@app.route('/sorry')
def sorry():
    return redirect(url_for('login')) 

if __name__ == '__main__':
   app.run(debug = True)