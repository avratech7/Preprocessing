import re
import string
#import nltk
#nltk.download('punkt')
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
stemmer = PorterStemmer()
#nltk.download('stopwords')
from nltk.corpus import stopwords
stopWords = set(stopwords.words('english'))


text = '''<p>I,m not and no Go dog dogs ,
 but if the bal and $%# 5nt and to doc
 so go and went store<p>	haa		is a fun story
 so we want the key cry cried <p>'''




def split_to_paragraphs(original_text):
	#if input with html <p> tags
	if re.match('<p>', original_text) != None:
		return original_text.split('<p>')
	#maybe need to be with split('\t')
	return original_text.split(' ')
	


def remove_not_letters(paragraph):
	words = paragraph.split(' ')
	#remove !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
	clean_text = [re.sub(r'[%s]' % re.escape(string.punctuation), '', word) for word in words]
	#remove words with digits 
	clean_text = [re.sub(r'\w*\d\w*', '', word) for word in clean_text]
	return ' '.join(clean_text)


def remove_whitespaces(paragraph):
	pass

'''
	Remove "Stop words" like "the", "on", "is". 
'''
def remove_stop_words(paragraph):
	
	return ' '.join([word for word in paragraph.split(' ') if word not in stopWords])
	


'''
	Stemming is a process of reducing words to their word stem, base or root form
'''
def stemming_the_paragraphs(paragraph):
	#https://tartarus.org/martin/PorterStemmer/
	#https://web.archive.org/web/20140827005744/http:/www.comp.lancs.ac.uk/computing/research/stemming/index.htm
	return ' '.join([stemmer.stem(word) for word in paragraph.split(' ')])
		

print([stemming_the_paragraphs(remove_stop_words(remove_not_letters(w))) for w in split_to_paragraphs(text) if w])
#print(stemming_the_paragraphs(' '.join([remove_stop_words(remove_not_letters(word)) for word in split_to_paragraphs(text)])))