from bs4 import BeautifulSoup as bs
import requests
import re
import string
import nltk
#nltk.download('punkt')
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
#nltk.download('stopwords')
from nltk.corpus import stopwords
stopWords = set(stopwords.words('english'))



def get_wiki_text(url):
	source = requests.get(url).text
	soup = bs(source, 'html.parser').find_all('p')
	return [par.text for par in soup]


def basic_clean(paragraph):
	words = paragraph.split(' ')	
	clean_text = [word.lower() for word in words]
	clean_text = [re.sub(r'\w*\d\w*', '', word) for word in clean_text]
	clean_text = [re.sub(r'[^a-zA-Z]', '', word) for word in clean_text]
	return ' '.join(clean_text)


def remove_stop_words(paragraph):
	return ' '.join([word for word in paragraph.split(' ') if word not in stopWords])


def stemming_the_paragraphs(paragraph):
	return ' '.join([stemmer.stem(word) for word in paragraph.split(' ')])


def get_clean_data(url, *label):
	return clean_paragraph(get_wiki_text(url), [stemming_the_paragraphs(remove_stop_words(basic_clean(p))) for p in get_wiki_text(url)],label, url)
	



class clean_paragraph():
	"""docstring for clean_paragraph"""
	def __init__(self, original_data, clean_data, label, url):
		self.original_data = original_data
		self.clean_data = clean_data
		self.label = label
		self.url = url



ssh = 'https://en.wikipedia.org/wiki/Secure_Shell'
#print(get_clean_data(ssh, 'cs').clean_data)
		
		

		



















