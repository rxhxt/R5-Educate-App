import sqlite3
import pandas as pd
import random
from datetime import datetime,timedelta
conn = sqlite3.connect('./data.db',check_same_thread=False)

class Fibonnacci():
    def get_Test(self,days,n=10):
        main_df = pd.read_sql("select * from personal",conn)
        print(main_df.columns)
        d = datetime.today() - timedelta(days=days)
        main_df = main_df[main_df['last_date_asked']!=d]
        print(main_df)
        questions_list = random.sample(list(main_df['question']),k=n)
        print(questions_list)
        A,B,C,D,ans = [],[],[],[],[]
        for quest in questions_list:
            temp = main_df[main_df['question']==quest].to_numpy()
            A.append(temp[0][3]) 
            B.append(temp[0][4])
            C.append(temp[0][5])
            D.append(temp[0][6])
            ans.append(temp[0][7])
            main_df._set_value(temp[0][0],'last_date_asked',datetime.now())
            main_df._set_value(temp[0][0],'times_asked',temp[0][9]+1)
            print(main_df)
        return questions_list,A,B,C,D,ans   
        

f = Fibonnacci()
# print(f.get_Test(2))
print(f.get_Test(3))