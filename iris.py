#!/usr/bin/python3

import time
from sklearn.datasets import load_iris
from sklearn import tree
#loading iris data

iris=load_iris()

fl_data=iris.data.tolist()
fl_target=iris.target.tolist()

setosa=fl_target[0:50]
train_set=setosa[0:49]

versicolor=fl_target[50:100]
train_vers=versicolor[0:49]

verginica=fl_target[100:150]
train_verg=verginica[0:49]

setosa=fl_data[0:50]
train_setosa=setosa[0:49]
test_setosa=setosa[-1]


versicolor=fl_data[50:100]
train_versicolor=versicolor[0:49]
test_versicolor=versicolor[2]

verginica=fl_data[100:150]
train_verginica=verginica[0:49]
test_verginica=verginica[-1]



features= train_setosa  + train_versicolor + train_verginica
output= train_set + train_vers + train_verg



algo=tree.DecisionTreeClassifier()
trained=algo.fit(features,output)
res=trained.predict([test_setosa,test_versicolor,test_verginica])
print (res)
