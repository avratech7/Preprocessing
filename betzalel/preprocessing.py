import string
#import nltk
#nltk.download('punkt')
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
stemmer = PorterStemmer()
import re
#---------------------------------------------------------------------------------------
from bs4 import BeautifulSoup as bs
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
source = requests.get('https://en.wikipedia.org/wiki/Basketball', headers=headers).text

soup = bs(source, 'html.parser')
p = soup.find_all('p')
to_str = ""
for par in p:
	to_str += (str(par))
	# print(to_str)
text = to_str

print('\n')
# text = 'sport teem in early December 1891, Canadian James Naismith,[4] a physical education professor and instructor at the International Young Men Christian Association Training School[5] (YMCA) (today, Springfield College) in Springfield, Massachusetts, was trying to keep his gym class active on a rainy day. He sought a vigorous indoor game to keep his students occupied and at proper levels of fitness during the long New England winters. After rejecting other ideas as either too rough or poorly suited to walled-in gymnasiums, he wrote the basic rules and nailed a peach basket onto a 10-foot (3.0 m) elevated track. In contrast with modern basketball nets, this peach basket retained its bottom, and balls had to be retrieved manually after each "basket" or point scored; this proved inefficient, however, so the bottom of the basket was removed, allowing the balls to be poked out with a long dowel each time.'
#-----------------------------------------------------------------------------------------------

from nltk.corpus import stopwords
stopWords = set(stopwords.words('english'))


def split_to_paragraphs(original_text):
	#if input with html <p> tags
	if re.match('<p>', original_text) != None:
		return original_text.split('<p>')
	#maybe need to be with split('\t')
	return original_text.split(' ')



# def remove_not_letters(paragraph):
# 	words = paragraph.split(' ')
# 	#remove !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# 	clean_text = [re.sub(r'[%s]' % re.escape(string.punctuation), '', word) for word in words]
# 	#remove words with digits
# 	clean_text = [re.sub(r'\w*\d\w*', '', word) for word in clean_text]
# 	return ' '.join(clean_text)
def remove_not_letters(paragraph):

	return ' '.join([re.sub('[^a-zA-Z]', '', word) for word in paragraph.split(' ')])

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


print(list(filter(None,[stemming_the_paragraphs(remove_stop_words(remove_not_letters(w))) for w in split_to_paragraphs(text)])))
#print(stemming_the_paragraphs(' '.join([remove_stop_words(remove_not_letters(word)) for word in split_to_paragraphs(text)])))


