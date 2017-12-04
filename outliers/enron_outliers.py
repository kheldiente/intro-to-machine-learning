#!/usr/bin/python

import pickle
import sys
import numpy
import matplotlib.pyplot as plt
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

### read in data dictionary, convert to numpy array
global data_dict, data
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop("TOTAL", 0) # remove TOTAL in data_dict
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

### your code below
for point in data:
    salaryPoint = point[0]
    bonusPoint = point[1]
    plt.scatter(salaryPoint, bonusPoint)

def getHighestOutlier():
    d = sorted(data, key=lambda x:x[1], reverse=True)
    for key in data_dict:
        dictSal = data_dict[key]["salary"]
        dictBonus = data_dict[key]["bonus"]
        pltSal = d[0][0] # the biggest Enron outlier with high salary
        pltBonus = d[0][1] # the biggest Enron outlier with high bonus
        # print "salary and bonus in data_dict of ", key, ": ", dictSal, "||", dictBonus
        sameSal = pltSal == dictSal
        sameBonus = pltBonus == pltBonus
        if sameSal and sameBonus:
            print "matched: ", key

getHighestOutlier()
plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()
# get 4 more outliers
for name in data_dict:
    # float() does not include NaN values
    mBonus = float(data_dict[name]["bonus"])
    mSalary = float(data_dict[name]["salary"])
    if mBonus >= 5000000 and mSalary >= 1000000:
        print name, "bonus: ", data_dict[name]["bonus"], "salary: ", data_dict[name]["salary"]
