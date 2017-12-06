""" if cannot import nltk run downloader to download all necessary packages """
# import nltk
# nltk.download()

from nltk.corpus import stopwords
sw = stopwords.words("english")
print "number of stopwords: ", len(sw)
print sw
