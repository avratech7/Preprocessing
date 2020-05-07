import re
import string
import nltk
#nltk.download('punkt')
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

text = '''<p>I,m not and no Go dog dogs ,
 but if the bal and $%# 5nt and to doc
 so go and went store<p>	haa		is a fun story
 so we want the key cry cried <p>'''

def split_paragraphs(text):
	return text.split('<p>')

def basic_clean(paragraphs):
	words = paragraphs.split(' ')
	clean_text = [re.sub(r'[%s]' % re.escape(string.punctuation), '', word) for word in words]
	#remove words with digits 
	clean_text = [re.sub(r'\w*\d\w*', '', word) for word in clean_text]
	return ' '.join(clean_text)

def stem_para(text):
	print(text)
	return ' '.join([stemmer.stem(word) for word in text.split(' ')])


print(stem_para(','.join([basic_clean(word) for word in split_paragraphs(text)])))