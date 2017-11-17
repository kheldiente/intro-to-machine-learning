#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
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
from sklearn.svm import SVC
print "features_train size: ", len(features_train), " || labels_train size: ", len(labels_train)
### for testing accuracy, half the data sets
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]
# print "after decreasing to smaller set => ", "features_train size: ", len(features_train), " || labels_train size: ", len(labels_train)
# clf = SVC(kernel='linear') # init SVC (support vector classifier) using linear kernel function
# clf = SVC() # init SVC using rbf kernel function by default
clf = SVC(C=10000.0) # init SVC with several C param values
t0 = time() # init runtime val
clf.fit(features_train, labels_train)
print "training time: ", round(time() - t0, 3), "s"
t0 = time() # reset runtime val to determine prediction runtime
# index = 50
pred = clf.predict(features_test)
print "predicting time: ", round(time() - t0, 3), "s"
from sklearn.metrics import accuracy_score
# print "predictions: ", pred[index]
print "number of Chris(1) class: ", list(pred).count(1) # convert numpy.ndarray to a list then get count of occurences of Chris(1) class
print "accuracy score :", accuracy_score(labels_test, pred)
#########################################################
