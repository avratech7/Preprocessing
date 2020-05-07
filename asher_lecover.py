import requests
from bs4 import BeautifulSoup as bs
from collections import Counter
import string
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
stemmer = PorterStemmer()
import re
from bs4 import BeautifulSoup as bs
import requests
from nltk.corpus import stopwords


url = "https://en.wikipedia.org/wiki/Basketball"
website = requests.get(url)
html_data_from_website = bs(website.content, 'html.parser')
stopWords = set(stopwords.words('english'))


#--------------------------------------------------------------------------------------------------
def only_visible_text(data, *subject):
    return [item.text for item in  html_data_from_website.findAll('p')]

#--------------------------------------------------------------------------------------------------
def remove_not_letters(paragraph):
    return ' '.join([re.sub('[^a-zA-Z]', '', word) for word in paragraph.split(' ')])
#-------------------------------------------------------------------------------------------------
'''
	Remove "Stop words" like "the", "on", "is".
'''
def remove_stop_words(paragraph):
	return ' '.join([word for word in paragraph.split(' ') if word not in stopWords])

'''
	Stemming is a process of reducing words to their word stem, base or root form
'''
def stemming_the_paragraphs(paragraph):
	return ' '.join([stemmer.stem(word) for word in paragraph.split(' ')])


def final_clean_data_function(data):
    pass

print(only_visible_text(html_data_from_website))
print([remove_not_letters(word) for word in only_visible_text(html_data_from_website)])
print([remove_stop_words(remove_not_letters(word)) for word in only_visible_text(html_data_from_website)])
print([stemming_the_paragraphs(remove_stop_words(remove_not_letters(word.lower()))) for word in only_visible_text(html_data_from_website)])