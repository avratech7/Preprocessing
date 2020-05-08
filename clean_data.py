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



def _get_wiki_text(url):
	source = requests.get(url).text
	soup = bs(source, 'html.parser').find_all('p')
	return [par.text for par in soup]


def _basic_clean(paragraph):
	words = paragraph.split(' ')	
	clean_text = [word.lower() for word in words]
	clean_text = [re.sub(r'\w*\d\w*', '', word) for word in clean_text]
	clean_text = [re.sub(r'[^a-zA-Z]', '', word) for word in clean_text]
	return ' '.join(clean_text)


def _remove_stop_words(paragraph):
	return ' '.join([word for word in paragraph.split(' ') if word not in stopWords])


def _stemming_the_paragraphs(paragraph):
	return ' '.join([stemmer.stem(word) for word in paragraph.split(' ')])


def get_clean_data(url, *label):
	origin_data = _get_wiki_text(url)
	return clean_paragraph(origin_data, [_stemming_the_paragraphs(_remove_stop_words(_basic_clean(p))) for p in origin_data],label, url)
	



class clean_paragraph():
	"""docstring for clean_paragraph"""
	def __init__(self, original_data, clean_data, label, url):
		self.original_data = original_data
		self.clean_data = clean_data
		self.label = label
		self.url = url
		self.list = [original_data, clean_data, label, url]


	def __iter__(self):
		return iter(self.list)


	def __add__(self, other):
		if (self.label == other.label):
			return clean_paragraph([*self.original_data, *other.original_data], [*self.clean_data, *other.clean_data], self.label, [self.url, other.url])


	def __getitem__(self, index):
		return self.list[index]


"""
ssh = 'https://en.wikipedia.org/wiki/Secure_Shell'
pyt = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
obj1 = get_clean_data(ssh, 'cs')
obj2 = get_clean_data(pyt, 'cs')
#print(list(get_clean_data(ssh, 'cs')))
newobj = obj1 + obj2
#print(newobj[3])

print(get_clean_data(ssh, 'cs')[0][0])
"""