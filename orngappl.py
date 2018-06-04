#!/usr/bin/python3

import sys

import sklearn
from sklearn import tree
inn=sys.argv
w=int(inn[1])
out=int(inn[2])

#print(type(w),type(out))

#apple & orange --texture,weight
#smooth=0  , bumpy=1

features=[[110,0],[120,0],[130,1],[140,1]]


output=["apple","apple","orange","orange"]

#now loading decision tree classifier

algo=tree.DecisionTreeClassifier()

#now training the features and output

trained=algo.fit(features,output)

#generaly looking for 1 core
#testing trained model

resoutput=trained.predict([[w,out]])

print(resoutput)
