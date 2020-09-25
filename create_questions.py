import spacy
import nltk
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize,sent_tokenize
from random import seed, randint
import requests
import json
import re
import random
from pywsd.similarity import max_similarity
from pywsd.lesk import adapted_lesk
from pywsd.lesk import simple_lesk
from pywsd.lesk import cosine_lesk
from nltk.corpus import wordnet as wn

# Using 'en_US' dictionary
# d = enchant.Dict("en_US")
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
	def get_distractors_wordnet(self,syn,word):
			distractors=[]
			word= word.lower()
			orig_word = word
			if len(word.split())>0:
				word = word.replace(" ","_")
			hypernym = syn.hypernyms()
			if len(hypernym) == 0: 
				return distractors
			for item in hypernym[0].hyponyms():
				name = item.lemmas()[0].name()
				#print ("name ",name, " word",orig_word)
				if name == orig_word:
					continue
				name = name.replace("_"," ")
				name = " ".join(w.capitalize() for w in name.split())
				if name is not None and name not in distractors:
					distractors.append(name)
			return distractors
		
	def get_wordsense(self,sent,word):
		word= word.lower()
		if len(word.split())>0:
			word = word.replace(" ","_")
		
		
		synsets = wn.synsets(word,'n')
		if synsets:
			wup = max_similarity(sent, word, 'wup', pos='n')
			adapted_lesk_output =  adapted_lesk(sent, word, pos='n')
			lowest_index = min (synsets.index(wup),synsets.index(adapted_lesk_output))
			return synsets[lowest_index]
		else:
			return None

	# Distractors from http://conceptnet.io/
	def get_distractors_conceptnet(self,word):
		word = word.lower()
		original_word= word
		if (len(word.split())>0):
			word = word.replace(" ","_")
		distractor_list = [] 
		url = "http://api.conceptnet.io/query?node=/c/en/%s/n&rel=/r/PartOf&start=/c/en/%s&limit=5"%(word,word)
		obj = requests.get(url).json()

		for edge in obj['edges']:
			link = edge['end']['term'] 

			url2 = "http://api.conceptnet.io/query?node=%s&rel=/r/PartOf&end=%s&limit=10"%(link,link)
			obj2 = requests.get(url2).json()
			for edge in obj2['edges']:
				word2 = edge['start']['label']
				if word2 not in distractor_list and original_word.lower() not in word2.lower():
					distractor_list.append(word2)
					
		return distractor_list
	def get_options(self,questions,answers):    		
		key_distractor_list = {}
		for Q,ans in zip(questions,answers):
			print(Q,ans)
			wordsense = qg.get_wordsense( Q,ans)
			if wordsense:
				distractors = qg.get_distractors_wordnet(wordsense, ans)
				if len(distractors) ==0:
					distractors = qg.get_distractors_conceptnet(ans)
				if len(distractors) != 0:
					key_distractor_list[ans] = distractors[0:4]
			else:
				distractors = qg.get_distractors_conceptnet( ans)
				if len(distractors) != 0:
					key_distractor_list[ans] = distractors[0:4]
			print(key_distractor_list)
		return(key_distractor_list)



    
text = '''The Tower Hill Memorial is a pair of Commonwealth War Graves Commission memorials in Trinity Square, on Tower Hill in London, England. The memorials, one for the First World War and one for the Second, commemorate more than 36,000 men and women of the Merchant 
Navy and fishing fleets who were killed as a result of enemy action and have no known grave. The dead are named on bronze panels ordered by the ships they served on. The first memorial, the Mercantile Marine War Memorial (pictured), was commissioned following the heavy losses sustained by merchant shipping in the First World War. It was designed by Sir Edwin Lutyens and unveiled by Queen Mary in 1928. The second, the Merchant Seamen's Memorial, is a semi-circular sunken garden designed by Sir Edward Maufe and unveiled by Queen Elizabeth II in November 1955. A third memorial,
 commemorating merchant sailors who were killed in the 1982 Falklands War, was added to the site in 2005. '''

qg = GenerateQuestions(text)
qg.get_ner()
questions_dict = qg.get_qna()
# print(questions_dict)
qg.get_options(questions_dict.keys(),questions_dict.values())