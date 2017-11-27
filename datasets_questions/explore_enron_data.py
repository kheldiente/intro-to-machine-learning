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

    def numberOfQuantifiedSalary(self):
        # no of dataset that has quantified salary
        result = 0
        for key in enron_data:
            obj = enron_data[key]
            salary_key = "salary"
            if salary_key in obj:
                salary = obj[salary_key]
                isNan = str(salary)
                if isNan != "NaN":
                    result += 1
        return result

    def numberOfQuantifiedTotalPayments(self):
        # no of dataset that has quantified salary
        result = 0
        for key in enron_data:
            obj = enron_data[key]
            total_payments_key = "total_payments"
            if total_payments_key in obj:
                total_payments = obj[total_payments_key]
                isNan = str(total_payments)
                if isNan != "NaN":
                    result += 1
        return result

    def numberOfKnownEmails(self):
        # no of dataset that has quantified salary
        result = 0
        for key in enron_data:
            obj = enron_data[key]
            email_key = "email_address"
            if email_key in obj:
                eadd = obj[email_key]
                isNan = str(eadd)
                if isNan != "NaN":
                    result += 1
        return result

    def getPercentageOfNanPayments(self):
        # percentage with NaN total_payments
        totalNoOfDataSet = self.getSizeOfData()
        totalNoOfQuantifiedTotalPayments = self.numberOfQuantifiedTotalPayments()
        percentage = (totalNoOfDataSet - totalNoOfQuantifiedTotalPayments * 1.0) / totalNoOfDataSet * 100
        return percentage

    def getPercentageOfNanPayments_POI(self):
        # percentage with NaN total_payments in regard in POIS
        # csv_poi_names = [name.replace(",", "").upper()  for name in self.getPOINames()]
        noOfNan = 0
        for name in self.getPOINames():
            name = name.replace(",","").upper()
            try:
                value = self.getValue(name, "total_payments")
                isNan = str(value) == "NaN"
                if isNan:
                    noOfNan += 1
            except Exception:
                pass
        return noOfNan

    def addBlankPeople(self, key):
        enron_data[key] = {'salary': 'NaN',
                'to_messages': 'NaN',
                'deferral_payments': 'NaN',
                'total_payments': 'NaN',
                'exercised_stock_options': 'NaN',
                'bonus': 'NaN',
                'restricted_stock': 'NaN',
                'shared_receipt_with_poi': 'NaN',
                'restricted_stock_deferred': 'NaN',
                'total_stock_value': 'NaN',
                'expenses': 'NaN',
                'loan_advances': 'NaN',
                'from_messages': 'NaN',
                'other': 'NaN',
                'from_this_person_to_poi': 'NaN',
                'poi': True,
                'director_fees': 'NaN',
                'deferred_income': 'NaN',
                'long_term_incentive': 'NaN',
                'email_address': 'blank@enron.com',
                'from_poi_to_this_person': 'NaN'}

enronDataObj = EnronData()
enronDataObj.loadData()
print "number of enron_data: ", enronDataObj.getSizeOfData()
# add 10 blank people
for x in range(10):
    enronDataObj.addBlankPeople(str(x))
print "number of new enron_data: ", enronDataObj.getSizeOfData()
print "number of features: ", enronDataObj.getSizeOfFeatures()
print "features: ", enronDataObj.getFeatures();
print "number of poi: ", enronDataObj.getNumberOfPois()
print "number of dataset that has quantified salary (!= NaN): ", enronDataObj.numberOfQuantifiedSalary()
print "number of known emails: ", enronDataObj.numberOfKnownEmails()
print "number of people with NaN total_payments: ", enronDataObj.getSizeOfData() - enronDataObj.numberOfQuantifiedTotalPayments()
print "percentage of people with NaN total_payments: ", enronDataObj.getPercentageOfNanPayments()
print "percentage of POIS with NaN total_payments: ", enronDataObj.getPercentageOfNanPayments_POI()
print "poi names: ", enronDataObj.getTotalPoisInFile()
print "stock of James Prentice: ", enronDataObj.getValue("PRENTICE JAMES", "total_stock_value")
print "emails of Wesley Colwell: ", enronDataObj.getValue("COLWELL WESLEY", "from_this_person_to_poi")
print "stock options of Jeffrey K Skilling: ", enronDataObj.getValue("SKILLING JEFFREY K", "exercised_stock_options")
