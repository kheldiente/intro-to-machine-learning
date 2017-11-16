#!/usr/bin/python

"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB() # init GaussianNB classifier
t0 = time() # init runtime val
clf.fit(features_train, labels_train) # then train data sets; features_train and labels_train
print "training time: ", round(time() - t0, 3), "s"
t0 = time() # reset runtime val
pred = clf.predict(features_test) # then predict using X = features_test
print "prediction time: ", round(time() - t0, 3), "s"
### import accuracy_score ###
from sklearn.metrics import accuracy_score
print "accuracy of author identifier: ", accuracy_score(labels_test, pred) # print accuracy of author identifier



#########################################################
