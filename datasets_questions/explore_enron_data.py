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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# counting the number of POIs and people with salaries or email addresses
totalPeople = 0
pois = 0
salaryied = 0
emailied = 0
totalPayments = 0
totalPaymentsPoi = 0

for key, value in enron_data.iteritems():
    totalPeople += 1

    if value["poi"]:
        pois += 1

        if value["total_payments"] == "NaN":
            totalPaymentsPoi += 1

    if value["salary"] != None and value["salary"] != "NaN" :
        salaryied += 1

    if value["email_address"] != None and value["email_address"] != "NaN":
        emailied += 1

    if value["total_payments"] == "NaN":
        totalPayments += 1

print("POIs:" + str(pois))
print("With salary: " + str(salaryied))
print("With email: " + str(emailied))
print("Percent without total payments: " + str((100.0 / totalPeople) * totalPayments))
print("Percent POI without total payments: " + str((100.0 / pois) * totalPaymentsPoi))
print("Total number of people are: " + str(totalPeople))
print("Total number of people with out payments are: " + str(totalPayments))

# getting the stock value of James Prentice
print(enron_data["PRENTICE JAMES"]["total_stock_value"])

# number of emails sent to Wesley Colwell
print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

# value of stock stock options exercised by Jeffrey Skilling
print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])
