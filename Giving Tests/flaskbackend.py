from flask import Flask, Response,redirect, url_for, request
import flask
import _sqlite3
from display_questions import StoreQuestions
import os


app = Flask(__name__, template_folder="templates",static_folder="static")
@app.route('/q=<int:q_id>',methods = ['POST', 'GET'])
def test_page2(q_id):
   if request.method == 'POST':
        user = request.form["SAE"]
        print(user)
   data = StoreQuestions().get_questions(5)
   q_id = q_id-1
   return flask.render_template('index.html', q_id = data['q_id'].unique()[q_id],
                                question = data['question'].unique()[q_id],
                                option_A = data['option_A'].unique()[q_id],
                                option_B = data['option_B'].unique()[q_id],
                                option_C = data['option_C'].unique()[q_id],
                                option_D = data['option_D'].unique()[q_id],)


if __name__ == '__main__':
   app.run(debug = True)