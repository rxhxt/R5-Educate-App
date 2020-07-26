from flask import Flask, Response,redirect, url_for, request
import flask
import _sqlite3
from display_questions import StoreQuestions
import os
from flask import Flask,render_template,url_for,request,jsonify,make_response,redirect
from flask_mysqldb import MySQL
import form
import yaml
from form import LoginForm
app = Flask(__name__, template_folder="templates",static_folder="static")
app.config['SECRET_KEY'] = 'you-will-never-guess'

db=yaml.load(open('db.yaml'))
app.config['MYSQL_HOST']=db['mysql_host']
app.config['MYSQL_USER']=db['mysql_user']
app.config['MYSQL_PASSWORD']=db['mysql_password']
app.config['MYSQL_DB']=db['mysql_db']

mysql=MySQL(app)



@app.route('/q=<int:q_id>',methods = ['POST', 'GET'])
def test_page2(q_id):
   if request.method == 'POST':
        user = request.form["SAE"]
        print(user)
   data = StoreQuestions().get_questions(5)
   q_id = q_id-1
   return flask.render_template('give_test.html', q_id = data['q_id'].unique()[q_id],
                                question = data['question'].unique()[q_id],
                                option_A = data['option_A'].unique()[q_id],
                                option_B = data['option_B'].unique()[q_id],
                                option_C = data['option_C'].unique()[q_id],
                                option_D = data['option_D'].unique()[q_id],)



@app.route('/')
def hello_world():
    return render_template('login.html')

#@app.route('/',methods=['post'])
#def login_cred():

#    return render_template('index.html')

@app.route('/',methods=["POST"])
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
        cur.execute("INSERT INTO user(acctype,name,email,password) VALUES(%s,%s,%s,%s)",(res['selectInput_d'],res['nameInput_d'],res['emailInput_d'],res['passwordInput_d']))
        mysql.connection.commit()
        cur.close()
    return redirect(url_for('first'))


@app.route('/success')
def first():
    return '<h1>Successs</h1>' 

@app.route('/sorry')
def sorry():
    return '<h1>Sorry !</h1>' 



if __name__ == '__main__':
   app.run(debug = True)