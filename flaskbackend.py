from flask import Flask, Response,redirect, url_for, request
import flask
# import summarize2.views as sv

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
# {% comment %} <form class="form-inline" action="http://localhost:5000/q={{ q_id }}" method="post"> {% endcomment %}
db=yaml.load(open('db.yaml'))
app.config['MYSQL_HOST']=db['mysql_host']
app.config['MYSQL_USER']=db['mysql_user']
app.config['MYSQL_PASSWORD']=db['mysql_password']
app.config['MYSQL_DB']=db['mysql_db']

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


@app.route('/login')
def login():
    return render_template('login.html')

#@app.route('/',methods=['post'])
#def login_cred():

#    return render_template('index.html')

@app.route('/login',methods=["POST"])
def create_entry():
    res=request.get_json()
    if res == None:
        usr=request.form['loginemail']
        passwd=request.form['loginPassword']
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM user")
        record=cur.fetchall()
        for row in record:
            if usr in row[2] and passwd in row[3]:
                print("here")
                return redirect(url_for('first'))
        mysql.connection.commit()
        cur.close()
        print(usr)
        return redirect(url_for('sorry'))

    else :
        print(res)
        print(res['emailInput_d'])
        cur=mysql.connection.cursor()
        global name, acc_holder
        name = res['nameInput_d']
        acc_holder = res['selectInput_d']
        cur.execute("INSERT INTO user(acctype,name,email,password) VALUES(%s,%s,%s,%s)",(res['selectInput_d'],res['nameInput_d'],res['emailInput_d'],res['passwordInput_d']))
        mysql.connection.commit()
        cur.close()
    return redirect(url_for('first'))


@app.route('/success')
def first():
    return redirect(url_for('my_dash_app')) 

@app.route('/sorry')
def sorry():
    return redirect(url_for('login')) 

if __name__ == '__main__':
   app.run(debug = True)