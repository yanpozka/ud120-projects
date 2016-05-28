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

enron_data = pickle.load(
    open("../final_project/final_project_dataset.pkl", "r"))

names_dict = {}

# for k in enron_data.keys():
#     parts = str(k).split()
#     if len(parts) < 2:
#         continue

#     result = parts[0] + " " + parts[1]
#     # print result
#     names_dict[result] = enron_data[k]['poi']


# with open("../final_project/poi_names.txt", "r") as f:
#     for line in f:
#         if line is None or line == "":
#             continue

#         parts = line.split()
#         if len(parts) < 3:
#             continue

#         p1 = parts[1]
#         name = (p1[:len(p1) - 1]).upper() + " " + parts[2].upper()

#         if name in names_dict and names_dict[name]:
#             count += 1

# print count
# James Prentice

# print enron_data["Skilling".upper() + " " + "Jeffrey".upper()]
# print enron_data["SKILLING JEFFREY K"]

count_p, ct = 0, 0
maxk, maxsalary = '', -1
secondk, secondsalary = '', -1

for k, p in enron_data.items():
    if k == "TOTAL":
        continue

    if p['salary'] != 'NaN':
        if p['salary'] > maxsalary:
            maxsalary = p['salary']
            maxk = k

        if p['salary'] > 1000000 and p['bonus'] > 5000000:
            print k, p['salary'], p['bonus']

    if p['poi']:
        count_p += 1

    if p['poi'] and p['total_payments'] == 'NaN':
        ct += 1


print maxk, maxsalary, secondk, secondsalary

# print (count_p * 100) / total
