# import nltk	
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')


from nltk import sent_tokenize, word_tokenize,RegexpTokenizer
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import re



f = open("wiki.raw", "r", encoding="utf8")
file_data = f.read()


# tokenization
words = word_tokenize(file_data)
print(words[:40])

#stop words removal and non english words removal
stop_words = set(stopwords.words("english"))
clean_words = RegexpTokenizer(r'\w+').tokenize(file_data)
words_without_stop_words = [word for word in clean_words if word not in stop_words]

# Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words_without_stop_words]
print(stemmed_words[:40])

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemitized_words = [lemmatizer.lemmatize(word) for word in words_without_stop_words]
print(lemitized_words[:40])
