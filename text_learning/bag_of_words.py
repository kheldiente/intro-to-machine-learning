from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
string1 = "hi Katie the self driving car will be late Best Sebastian"
string2 = "Hi Sebastian the machine learning class will be great great great Best Katie"
string3 = "Hi Katie the machine learning class will be most excellent"
email_list = [string1, string2, string3]
bag_of_words = vectorizer.fit(email_list)
bag_of_words = vectorizer.transform(email_list)
print bag_of_words
### output ###
# (0, 0)        1 => (document number 0, word number 0)   occurs 1 time
# (0, 1)        1
# (0, 2)        1
# (0, 4)        1
# (0, 7)        1
# (0, 8)        1
# (0, 9)        1
# (0, 13)       1
# (0, 14)       1
# (0, 15)       1
# (0, 16)       1
# (1, 0)        1
# (1, 1)        1
# (1, 3)        1
# (1, 6)        3 => (document number 1, word number 6)   occurs 3 times
# (1, 7)        1
# (1, 8)        1
# (1, 10)       1
# (1, 11)       1
# (1, 13)       1
# (1, 15)       1
# (1, 16)       1
# (2, 0)        1
# (2, 3)        1
# (2, 5)        1
# (2, 7)        1
# (2, 8)        1
# (2, 10)       1
# (2, 11)       1
# (2, 12)       1
# (2, 15)       1
# (2, 16)       1
