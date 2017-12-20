#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)

### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl"
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()
### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]
features = vectorizer.get_feature_names()
print "feature size: ", len(features)

### getting the most important word using decisiontree classifier
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
from sklearn.metrics import accuracy_score
print "accuracy score in classifier: ", accuracy_score(labels_test, pred)

feature_imp = clf.feature_importances_
sorted_feature_imp = sorted(feature_imp, key=float)
most_imp_word_percentage = sorted_feature_imp[len(feature_imp) - 1]
most_imp_word = ""
print "percentage", most_imp_word_percentage
for index in range(len(feature_imp) - 1):
    if feature_imp[index] == most_imp_word_percentage:
        print "index: ", index, " => ", feature_imp[index]
        most_imp_word = features[index] # get from the generated features from tfidf vectorizer
print "feauture_importances: ", most_imp_word

### your code goes here
from sklearn.tree import DecisionTreeRegressor
reg = DecisionTreeRegressor()
reg.fit(features_train, labels_train)
pred = reg.predict(features_test)
from sklearn.metrics import accuracy_score
print "accuracy score in regression: ", accuracy_score(labels_test, pred)
