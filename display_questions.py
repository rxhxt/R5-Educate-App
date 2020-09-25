import sqlite3
import pandas as pd
from datetime import datetime
pd.set_option('display.max_columns', None)
conn = sqlite3.connect('./data2.db',check_same_thread=False)

class StoreQuestions():
    #To Add Questions to the DB
    def input_questions(self,q_id,question,option_list,answer,teacher):
       df =  pd.DataFrame(columns=['q_id','question', 'option_A', 'option_B', 'option_C', 'option_D',
       'correct_answer', 'times_asked ', 'last_date_asked', 'times_correct',
       'times_wrong', 'teacher'])
       df['id'] = q_id
       df['question'] = question
       df['option_A'],df['option_B'],df['option_C'],df['option_D'] = option_list[0],option_list[1],option_list[2],option_list[3]
       df['correct answer'] = answer
       df['times_asked'],df['times_correct'],df['times_wrong'] = 0,0,0
       df['teacher'] = teacher
       df.to_sql('questions',conn,if_exists='append',index=False)
       return "DONE"
    # To get a certain amount of questions
    def get_questions(self,count):
        data = pd.read_sql('Select q_id,question,option_A,option_B,option_C,option_D,correct_answer from questions', conn)
        if data.shape[0]>count:return data.iloc[0:count,:]
        else:return data
    #to store the answered results
    def store_results(self,iscorrect, qid):
        qid = qid +1
        query = 'Select * from questions where q_id like ' + str(qid)
        cursor = conn.cursor()
        data = pd.read_sql(query, conn)
        # print(data.head())
        data_list = data.values.ravel()
        # print(len(data_list))
        query2 = ""
        if iscorrect:
            query2 = (f'''UPDATE questions SET times_correct = {data_list[9] + 1},
                   last_date_asked = "{datetime.today().strftime('%Y-%m-%d')}", "times_asked " = {data_list[7]+1}
                    WHERE q_id like {qid} ''')
        else:
            query2 = (f'''UPDATE questions SET times_correct = {data_list[10] + 1},
                               last_date_asked = "{datetime.today().strftime('%Y-%m-%d')}", "times_asked " = {data_list[7] + 1}
                                WHERE q_id like {qid} ''')
        cursor.execute(query2)
        conn.commit()
        query = 'Select * from questions where q_id = ' + str(qid)
        data = pd.read_sql(query, conn)
        # print(data.to_dict())


# Q = StoreQuestions()
# # Q.input_questions("Victoria Day is a public holiday and is celebrated each year in",['Canada','New Zealand','United States','United Kingdom'],'Canada','Himani')
# # Q.store_results(True,"Victoria Day is a public holiday and is celebrated each year in")
# print(Q.get_questions(1))
# # Q.store_results(True, 3)