import requests
from bs4 import BeautifulSoup as bs
from collections import Counter
import string
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import re
from bs4 import BeautifulSoup as bs
import requests
from nltk.corpus import stopwords


class Preprocessing:

    def __init__(self, url, label):
        self.url = url
        self.label = label

    def porterStemmer(self):
        stemmer = PorterStemmer()
        return stemmer

    def convert_from_url_to__html(self, url):
        website = requests.get(self.url)
        html_data_from_website = bs(website.content, 'html.parser')
        return html_data_from_website

    # --------------------------------------------------------------------------------------------------
    def only_visible_text(self, url, *subject):
        data = self.convert_from_url_to__html(self.url)
        result = [item.text for item in data.findAll('p')]
        for i in result:
            str(result)
        return result

    # --------------------------------------------------------------------------------------------------
    def remove_not_letters(self, url):
        paragraph = self.only_visible_text(self.url)
        return ' '.join([re.sub('[^a-zA-Z]', '', word) for word in paragraph.split(' ')])
    # -------------------------------------------------------------------------------------------------
    '''
    	Remove "Stop words" like "the", "on", "is".
    '''

    def remove_stop_words(self, paragraph):
        stopWords = set(stopwords.words('english'))
        return ' '.join([word for word in paragraph.split(' ') if word not in stopWords])

    '''
    	Stemming is a process of reducing words to their word stem, base or root form
    '''

    def stemming_the_paragraphs(self, paragraph):
        return ' '.join([self.porterStemmer().stem(word) for word in paragraph.split(' ')])

    def final_clean_data_function(self, data, orignal_data, label):
        return [self.stemming_the_paragraphs(self.remove_stop_words(self.remove_not_letters(word.lower()))) for word in self.only_visible_text(self.html_data_from_website)]


url = 'https://en.wikipedia.org/wiki/Basketball'
preprocessing1 = Preprocessing(url,'sport')

# print(preprocessing1.only_visible_text(url))
# print(preprocessing1.only_visible_text(url))
print(preprocessing1.remove_not_letters(url))
# print(preprocessing1.final_clean_data_function(html_data_from_website, 'aaa', 'bbb'))
# print(preprocessing1.only_visible_text(html_data_from_website))

