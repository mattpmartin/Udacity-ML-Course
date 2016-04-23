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

#creating our object to store our data in
gnb = GaussianNB()

#timeing tests
t0 = time()

#actually training our object
gnb.fit(features_train, labels_train)

#printing out the performance
print "training time:", round(time()-t0, 3), "s"

#checking the perdiction time
t0 = time()
print "a perdiction:", gnb.predict(features_test[0])
print "perdict time:", round(time()-t0, 3), "s"

#printing out the accuracy
print "The maching is ", gnb.score(features_test, labels_test), "accurate"

#########################################################
