import spacy
from spacy import displacy
from collections import Counter
from nltk.tokenize import word_tokenize,sent_tokenize
from random import seed, randint
import enchant

# Using 'en_US' dictionary
d = enchant.Dict("en_US")
# seed random number generator
seed(1)
nlp = spacy.load('en_core_web_sm')

class GenerateQuestions:
    def __init__(self,text):
        self.text = text
    #To identify the entities
    def get_ner(self):
        doc = nlp(self.text)
        self.entity_dict = [{'word':X.text,'label':X.label_} for X in doc.ents]
        return  self.entity_dict
    # to get the dictionary containing question and answers
    def get_qna(self):
        # https://spacy.io/api/annotation#named-entities

        sentences = sent_tokenize(self.text)
        itr = 0
        flag = 0
        options_list = []
        temp = []
        for line in self.entity_dict:
            if line['word'] in sentences[itr]:
                temp.append(line['word'])
            else:
                options_list.append(temp)
                temp = []
                itr = itr + 1
        qna = {}
        itr = 0
        for sentence in sentences:
            try:
                if len(options_list[itr]) > 0:
                    answer = options_list[itr][randint(0, len(options_list[itr])-1)]
                    question = sentence.replace(answer, "________________")
                    qna[question] = answer
                    itr = itr + 1
            except IndexError:
                pass
        return qna
    def get_options(self,ans):
        print(d.suggest(ans))



text = '''The Fourth Test of the 1948 Ashes series was one of five Tests in a cricket series between Australia and England. Played at Headingley Stadium at Leeds from 22 to 27 July, for the third time in a row the match set a new record for the highest attendance at a Test in England. On the last day, Australia, captained by Don Bradman (pictured), had a target of 404 to make up, and England had used a heavy roller to break up the pitch to make batting harder. Although many observers predicted that England would win easily on a deteriorating surface, Australia put together a stand of 301 in only 217 minutes, aided by erratic bowling and several missed catches and stumpings. Australia won the match by seven wickets with 15 minutes remaining to take an unassailable 3–0 series lead. In successfully chasing a target of 404, they set a new world record for the highest victorious runchase in Test history. '''

qg = GenerateQuestions(text)
qg.get_ner()
questions_dict = qg.get_qna()
print(questions_dict)
