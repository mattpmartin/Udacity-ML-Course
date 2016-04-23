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
from sklearn import svm

clf = svm.SVC(kernel="rbf", C=10000)

#make the training dataset smaller

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

# t0 = time()
clf.fit(features_train, labels_train)
# print("The training time was:", (time() - t0))
#
# t1 = time()
# print("Acuracy of SVM is: ", clf.score(features_test, labels_test))
# print("The comparision time was:", (time() - t1))

#making perdictions for certin cases
# print("Perdicted result:", clf.predict([features_test[10]])[0])
# print("Actual result:", labels_test[10])
#
# print("Perdicted result:", clf.predict([features_test[26]])[0])
# print("Actual result:", labels_test[26])
#
# print("Perdicted result:", clf.predict([features_test[50]])[0])
# print("Actual result:", labels_test[50])

#count number of perdictions
perdictions = clf.predict(features_test)

chrisPerdicted = 0

for x in perdictions:
    if x == 1: chrisPerdicted += 1

print("chris is perdicted to have send ", chrisPerdicted, "emails")

#########################################################
