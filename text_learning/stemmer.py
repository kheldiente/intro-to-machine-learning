""" stem or get the root word of words e.g response, respond, unresponsiveness => respon is the root word """

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
print stemmer.stem("responsiveness")
print stemmer.stem("responsivity")
print stemmer.stem("unresponsive")
