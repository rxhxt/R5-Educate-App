import sqlite3
import pandas as pd
import random
from datetime import datetime,timedelta
conn = sqlite3.connect('./data2.db',check_same_thread=False)

class Fibonnacci():
    def get_Test(self,days,n=10):
        main_df = pd.read_sql("select * from questions",conn)
        print(main_df['question'].shape)
        print(main_df.columns)
        d = datetime.today() - timedelta(days=days)
        main_df = main_df[main_df['last_date_asked']!=d]
        questions_list = random.sample(list(main_df['question']),k=n)
        A,B,C,D,ans = [],[],[],[],[]
        for quest in questions_list:
            temp = main_df[main_df['question']==quest]
            A.append(temp.loc[:,'option_A']) 
            B.append(temp.loc[:,'option_B'])
            C.append(temp.loc[:,'option_C'])
            D.append(temp.loc[:,'option_D'])
            ans.append(temp.loc[:,'correct_answer'])
            main_df[main_df['question']==quest].loc[:,'las_date_asked'] = datetime.now()
        return questions_list,A,B,C,D,ans
        

