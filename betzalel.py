import re
import string
import nltk
#nltk.download('punkt')
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
def clean_data(text, *label):

	clean_text = text.split('\t')
	
	#Make all lower
	clean_text = list(map(str.lower ,clean_text))	
	#remove text in square brackets
	clean_text = [re.sub(r'\[.*?\]', '', word) for word in clean_text]
	# #remove punctuation
	clean_text = [re.sub(r'[%s]' % re.escape(string.punctuation), '', word) for word in clean_text]
	# #remove words with digits 
	clean_text = [re.sub(r'\w*\d\w*', '', word) for word in clean_text]
	
	clean_text = list(map(stemmer.stem,[word for word in clean_text]))

	return clean_text


#print(clean_data('English I i\'m not and no dog dogs 43rg &%^ hg56 [sht] with A HELLO (no) 5rh		 #@%$^%$'))
#print(nltk.word_tokenize("was'nt in my Case I my i I'm not no"))
print(string.punctuation)