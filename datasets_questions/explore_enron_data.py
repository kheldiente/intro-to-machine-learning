#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

class EnronData:

    def loadData(self):
        global enron_data
        enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

    def getNumberOfPois(self):
        # no of poi that is equals to 1
        result = 0
        for key in enron_data:
            obj = enron_data[key]
            poi_key = "poi"
            if poi_key in obj:
                poi = obj[poi_key]
                if poi == 1:
                    result += 1
        return result

    def getSizeOfData(self):
        return len(enron_data)

    def getSizeOfFeatures(self):
        return len(enron_data["SKILLING JEFFREY K"])

    def getFeatures(self):
        return enron_data["SKILLING JEFFREY K"]

    def getTotalPoisInFile(self):
        poi_names = self.getPOINames()
        return len(poi_names)

    def getPOINames(self):
        poi_names = []
        with open("../final_project/poi_names.txt", "r") as fo:
            for line in fo.readlines():
                try:
                    open_paren = line[0]
                    close_paren = line[2]
                    if(open_paren == "(" and close_paren == ")"):
                        poi_names.append(line[4:].splitlines()[0]) # splitness() removes \n in text
                except Exception:
                    pass
        return poi_names

    def getValue(self, key, feature):
        return enron_data[key][feature]


enronDataObj = EnronData()
enronDataObj.loadData()
print "number of enron_data: ", enronDataObj.getSizeOfData()
print "number of features: ", enronDataObj.getSizeOfFeatures()
print "features: ", enronDataObj.getFeatures();
print "number of poi: ", enronDataObj.getNumberOfPois()
print "poi names: ", enronDataObj.getTotalPoisInFile()
print "stock of James Prentice: ", enronDataObj.getValue("PRENTICE JAMES", "total_stock_value")
print "emails of Wesley Colwell: ", enronDataObj.getValue("COLWELL WESLEY", "from_this_person_to_poi")
print "stock options of Jeffrey K Skilling: ", enronDataObj.getValue("SKILLING JEFFREY K", "exercised_stock_options") 
