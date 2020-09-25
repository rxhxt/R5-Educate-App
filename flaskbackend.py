from flask import render_template, request, flash, redirect, url_for,send_from_directory
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
# from display_questions import StoreQuestions
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
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config["PDF_UPLOADS"] = "static/pdf/uploads"
app.config["UPLOAD_FOLDER"] = 'static/notes/uploads'
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

# mysql=MySQL(app)
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

class QuestionForm(FlaskForm):
    question=StringField('Question', validators=[DataRequired()])
    option_1=StringField('Option 1', validators=[DataRequired()])
    option_2=StringField('Option 2', validators=[DataRequired()])
    option_3=StringField('Option 3', validators=[DataRequired()])
    option_4=StringField('Option 4', validators=[DataRequired()])
    correct_ans=StringField('Type the correct Answer', validators=[DataRequired()])
    submit=SubmitField('Add Question')
    


class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    typeOfUser=db.Column(db.String(10), nullable=False)
    name=db.Column(db.String(150), nullable=False)
    image_file=db.Column(db.String(20), nullable=False,default='default.jpeg')
    email=db.Column(db.String(120), nullable=False, unique=True)
    password=db.Column(db.String(60), nullable=False)
    date_registered=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    loginLog=db.relationship('Log', backref='user')
    SummarizerLog=db.relationship('Summarizer', backref='user')
    testsCreated=db.relationship('Tests', backref='user')
    testsGiven=db.relationship('History', backref='user')
    uploads=db.relationship('Uploads', backref='user')
    transactions=db.relationship('Transactions', backref='user')
    personalQuestions=db.relationship('Personal', backref='user')


    # def __repr__(self):
    #     return f"User('{self.name}', '{self.email}')"

class Log(db.Model, UserMixin):
	session_id=db.Column(db.Integer, primary_key=True)
	user_id=db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
	login_time=db.Column(db.DateTime, nullable=False,default=datetime.utcnow )
	logout_time=db.Column(db.DateTime, nullable=False,default=datetime.utcnow)


class Summarizer(db.Model, UserMixin):
	request_id=db.Column(db.Integer, primary_key=True)
	user_id=db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
	email=db.Column(db.String(120), nullable=False)
	time_when_requested=db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
	file_name=db.Column(db.String(200), nullable=False)



class Tests(db.Model, UserMixin):
	test_id=db.Column(db.Integer, primary_key=True)
	test_name=db.Column(db.String(150), nullable=False)
	test_creator=db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
	date_created=db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

	QuestionList=db.relationship('Questions', backref='questions')
	TakenBy=db.relationship('History', backref='test')


class Questions(db.Model, UserMixin):
	question_id=db.Column(db.Integer, primary_key=True)
	test_id=db.Column(db.Integer, db.ForeignKey("tests.test_id"), nullable=False)
	question=db.Column(db.Text, nullable=False)
	option_1=db.Column(db.Text, nullable=False)
	option_2=db.Column(db.Text, nullable=False)
	option_3=db.Column(db.Text, nullable=False)
	option_4=db.Column(db.Text, nullable=False)
	correct_option=db.Column(db.Text, nullable=False)

class History(db.Model,UserMixin):
	history_id=db.Column(db.Integer, primary_key=True)
	user_id=db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
	test_id=db.Column(db.Integer, db.ForeignKey("tests.test_id"), nullable=False)
	score=db.Column(db.Integer, nullable=False)
	start_time=db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
	end_time=db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

class Personal(db.Model,UserMixin):
	question_id=db.Column(db.Integer, primary_key=True)
	user_id=db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
	question=db.Column(db.Text, nullable=False)
	option_1=db.Column(db.Text, nullable=False)
	option_2=db.Column(db.Text, nullable=False)
	option_3=db.Column(db.Text, nullable=False)
	option_4=db.Column(db.Text, nullable=False)
	correct_option=db.Column(db.Text, nullable=False)
	timesAsked=db.Column(db.Integer, nullable=False)
	timesCorrect=db.Column(db.Integer, nullable=False)
	last_date_asked=db.Column(db.DateTime, nullable=False)

class Uploads(db.Model,UserMixin):
	upload_id=db.Column(db.Integer, primary_key=True)
	name=db.Column(db.String(150), nullable=False)
	uploaded_by=db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
	time_uploaded=db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
	message=db.Column(db.Text,nullable=True)


class Transactions(db.Model,UserMixin):
	transaction_id=db.Column(db.Integer, primary_key=True)
	timestamp=db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
	user_id=db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
	transaction_type=db.Column(db.String(100), nullable=False)







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
@app.route("/", methods=['POST', 'GET'])
def signup():
    if current_user.is_authenticated:
        return redirect("login.html")
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(typeOfUser=form.typeOfUser.data, name=form.name.data, email=form.email.data, password=hashed_password)
        success=0
        try:
            db.session.add(user)
            db.session.commit()
            success=1
        except:
            flash(f'The user is already registered!! Try to login!!', category='danger') 
        if success==1:
            no=User.query.filter_by(email=form.email.data).first().id
            t1=Transactions(user_id=no,transaction_type='Registration')
            db.session.add(t1)
            db.session.commit()    
            flash(f'Account Created for {form.name.data}!, you can now login :)', category='success')
            return redirect(url_for('login'))   
    return render_template('signup.html', form=form)


@app.route('/dashboard_student',methods = ['POST', 'GET'])
@login_required
def dashboard_student():
    send_list = str("0, 10, 12, 14, 16, 20, 20, 25, 30")
    pie_list = str("65, 35")
    bar_list = str("40, 50,20 ,10,80,90,98,20,75,64,20,84,65,45,80")
    # print(str(send_list))
    if request.method == 'POST':
        return render_template('dash_s.html',hc = str(send_list),datapie= str(pie_list), databar=str(bar_list))
    return render_template('dash_s.html',hc = str(send_list), datapie = str(pie_list),databar=str(bar_list))

@app.route("/dashboard_teacher", methods=['GET', 'POST'])
@login_required
def dashboard_teacher():
    return render_template("layout_teacher.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard_student'))
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
            no=user.id
            t1=Transactions(user_id=no,transaction_type='Login')
            db.session.add(t1)
            db.session.commit()   
            if next_page:
                return redirect(next_page)
            else:
                print("Logged In")
                if user.typeOfUser=='Student':
                    return redirect(url_for('dashboard_student'))
                else:
                    return redirect(url_for('dashboard_teacher'))    

                    
        else:
            flash(f'Login Unsuccessful. Please check the email and/or Password', 'danger')  
              
    return render_template('login.html', form=form)




@app.route('/tests', methods=['GET', 'POST'])
@login_required
def testCover():
    form=QuestionForm()
    if form.validate_on_submit():
        print(current_user.id)
        print(form.question.data)
        print(form.option_1.data)
        p1=Personal(user_id=current_user.id, question=form.question.data, option_1=form.option_1.data, option_2=form.option_2.data, option_3=form.option_3.data, option_4=form.option_4.data, correct_option=form.correct_ans.data, timesCorrect=0, timesAsked=0)
        t1=Transactions(user_id=current_user.id,transaction_type='Add A Question')
        try:
            db.session.add(p1)
            db.session.add(t1)
            db.session.commit()
            flash(f'Your Question was added to your Personal TRAIN Test Database')

            return redirect(url_for('testCover'))
        except:
            flash(f'We could not add your question!! Please Try Again!')  
            return redirect(url_for('testCover'))  
    return render_template('testcover.html', form=form)



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



@app.route("/profile_student", methods=['GET', 'POST'])
@login_required
def profile_student():
    return render_template('profile_student.html', user=current_user)

def allowed_pdf(filename):
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    if ext.upper() in app.config["ALLOWED_EXTENSIONS"]:
        return True
    return False

@app.route("/notification-student", methods=['GET'])
@login_required
def notifications_student():
    uploads=[]
    u=Uploads.query.all()
    for upload in u:
        by=upload.uploaded_by
        uu=User.query.filter_by(id=by).first()
        l=[upload.name, upload.time_uploaded, upload.message,uu.name]
        uploads.append(l)
    return render_template("notification_student.html", uploads=uploads)

@app.route("/notification-teacher", methods=['GET'])
@login_required
def notifications_teacher():
    summaries=[]
    s=Summarizer.query.all()
    for summary in s:
        by=summary.user_id
        uu=User.query.filter_by(id=by).first()
        l=[summary.email, summary.time_when_requested, summary.file_name,uu.name]
        summaries.append(l)
    return render_template("notification_teacher.html", summaries=summaries)    

@app.route('/download', methods=['GET', 'POST'])
@login_required
def download():    
    print("cid="+str(current_user.id))
    id = request.args['id']
    print(id)
    t1=Transactions(user_id=current_user.id, transaction_type='Download PDF')
    db.session.add(t1)
    db.session.commit()
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename=id, as_attachment=True)

@app.route('/upload-notes', methods=['GET', 'POST'])
@login_required
def upload_notes():
    if request.method == "POST":
        if request.files:
            pdf = request.files["pdf"]
            message = request.form['textarea2']

            if pdf.filename == "":
                return render_template('upload_notes.html', logs=current_user.uploads)
            if not allowed_pdf(pdf.filename):
                return render_template('upload_notes.html', logs=current_user.uploads)
            else:
                print(pdf.filename)
                print(message)
                u1=Uploads(name=pdf.filename, uploaded_by=current_user.id, message=message)
                t1=Transactions(user_id=current_user.id, transaction_type='Upload Notes')
                db.session.add(u1)
                db.session.add(t1)
                db.session.commit()
                pdf.save(os.path.join(app.config["UPLOAD_FOLDER"] , pdf.filename))
                return render_template('upload_notes.html', logs=current_user.uploads)
        return redirect(request.url)
    return render_template('upload_notes.html', logs=current_user.uploads)                               



@app.route('/upload-pdf', methods=["GET", "POST"])
def upload_pdf():
    uploads=[]
    u=Uploads.query.all()
    for upload in u:
        by=upload.uploaded_by
        uu=User.query.filter_by(id=by).first()
        l=[upload.name, upload.time_uploaded, upload.message,uu.name]
        uploads.append(l)
    if request.method == "POST":
        if request.files:
            pdf = request.files["pdf"]
            mail = request.form['email']

            if pdf.filename == "":
                return render_template('upload_pdf.html', logs=current_user.SummarizerLog, uploads=uploads)
            if not allowed_pdf(pdf.filename):
                return render_template('upload_pdf.html', logs=current_user.SummarizerLog, uploads=uploads)
            else:
                print(pdf.filename)
                s1=Summarizer(user_id=current_user.id,email=mail, file_name=pdf.filename)
                filename = 'pdf_file.pdf'
                pdf.save(os.path.join(app.config["PDF_UPLOADS"], filename))
                thread = Thread(target = pdfParser, kwargs={'filename': os.path.join(app.config["PDF_UPLOADS"], 'pdf_file.pdf'), 'mailid': f'{mail}'})
                t1=Transactions(user_id=current_user.id,transaction_type='Summarized')
                db.session.add(t1)
                db.session.add(s1)
                db.session.commit()

                thread.start()
                return render_template('upload_pdf.html',logs=current_user.SummarizerLog, uploads=uploads)
        return redirect(request.url)
    return render_template('upload_pdf.html', logs=current_user.SummarizerLog, uploads=uploads)





@app.route('/submitted',methods = ['POST', 'GET'])
def submission():
    if request.method == 'POST':
        return redirect(url_for('hello_world'))
    global name
    return flask.render_template('success.html',name = name)

@app.route('/logout')
def logout():
    no=current_user.id
    print(no)
    t1=Transactions(user_id=no,transaction_type='Logout')
    db.session.add(t1)
    db.session.commit()
    loginTime=Transactions.query.filter_by(transaction_type='Login').filter_by(user_id=no).order_by(Transactions.timestamp.desc()).first().timestamp
    print(loginTime)
    l1=Log(user_id=no, login_time=loginTime)  
    db.session.add(l1)
    db.session.commit()
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