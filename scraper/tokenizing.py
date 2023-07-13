import nltk
# nltk.download('punkt')
# nltk.download("stopwords")
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('words')
# nltk.download('maxent_ne_chunker')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.stem import WordNetLemmatizer
import requests
from bs4 import BeautifulSoup


lemmatizer = WordNetLemmatizer()

snow_stemmer = SnowballStemmer(language='english')
stemmer = PorterStemmer()

example_string = """
Muad'Dib learned rapidly because his first training was in how to learn.
And the first lesson of all was the basic trust that he could learn.
It's shocking to find how many people do not believe they can learn,
and how many more believe learning to be difficult."""

# for i in word_tokenize(example_string):
#     print(i)

### PORTER STEMMER AND STOPWORDS
worf_quote = "Sir, I protest. I am not a merry man!"
words_in_quote = word_tokenize(worf_quote)
stop_words = set(stopwords.words("english"))

filtered_list = [word for word in words_in_quote if word.casefold() not in stop_words]
# print(filtered_list)

### STEMMING USING SNOWBALL / PORTER2

string_for_stemming = """
The crew of the USS Discovery discovered many discoveries.
Discovering is what explorers do."""

word_stem = word_tokenize(string_for_stemming)

stemmed_words = [snow_stemmer.stem(word) for word in word_stem]
# print(stemmed_words)

sagan_quote = """
If you wish to make an apple pie from scratch,
you must first invent the universe."""

words_pos = word_tokenize(sagan_quote)
# print(nltk.pos_tag(words_pos))

# print(lemmatizer.lemmatize('scarves'))


### LEMMATIZING

string_for_lemmatizing = "The friends of DeSoto love scarves."

word_lemm = word_tokenize(string_for_lemmatizing)

lemm_list = [lemmatizer.lemmatize(word) for word in word_lemm]
# print(lemm_list)

### CHUNKING

lotr_quote = "It's a dangerous business, Frodo, going out your door."

word_chunk = word_tokenize(lotr_quote)

### NER Chunking

quote = """
Men like Schiaparelli watched the red planet—it is odd, by-the-bye, that
for countless centuries Mars has been the star of war—but failed to
interpret the fluctuating appearances of the markings they mapped so well.
All that time the Martians must have been getting ready.

During the opposition of 1894 a great light was seen on the illuminated
part of the disk, first at the Lick Observatory, then by Perrotin of Nice,
and then by other observers. English readers heard of it first in the
issue of Nature dated August 2."""

words_ner = word_tokenize(quote)
ner_pos = nltk.pos_tag(words_ner)
tree = nltk.ne_chunk(ner_pos,binary=True) #named entities won't be labeled more specifically
l = set(' '.join(i[0]for i in t) for t in tree if hasattr(t,'label') and t.label() == 'NE')
# print(l)
# text8.concordance('man')


