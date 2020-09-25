import sqlite3
import pandas as pd
import random
from datetime import datetime,timedelta
conn = sqlite3.connect('./data2.db',check_same_thread=False)

class Fibonnacci():
    def get_Test(self,last_test_days,n=10):
        main_df = pd.read_sql("select * from questions",conn)
        print(main_df.columns)
        d = datetime.today() - timedelta(days=last_test_days)
        main_df = main_df[main_df['last_date_asked']!=d]
        questions_list = random.sample(list(main_df['question']),k=n)
        A,B,C,D,ans = [],[],[],[],[]
        for quest in questions_list:
            temp = main_df[main_df['question']==quest].to_numpy()
            A.append(temp[0][2]) 
            B.append(temp[0][3])
            C.append(temp[0][4])
            D.append(temp[0][5])
            ans.append(temp[0][6])
            main_df._set_value(temp[0][0],'last_date_asked',datetime.now())
            main_df._set_value(temp[0][0],'times_asked',temp[0][7]+1)
        return questions_list,A,B,C,D,ans   
        

f = Fibonnacci()
# print(f.get_Test(2))
questions_list,A,B,C,D,ans   = f.get_Test(3)
print(A)
print(type(A))