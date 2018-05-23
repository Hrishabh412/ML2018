#!/usr/bin/python3

from sklearn.datasets import load_iris

from sklearn.neighbors import KNeighborsRegressor


iris=load_iris()

import numpy as np

x=[0,50,100]

train_data=np.delete(iris.data,x,axis=0)

test_data=iris.data[x]

train_target=np.delete(iris.target,x)
test_target=iris.target[x]

#loading KNN algo

from sklearn.neighbors import KNeighborsClassifier

#calling algo

clf=KNeighborsClassifier(n_neighbors=3)
#training datasets

knn_trained=clf.fit(train_data,train_target)

#predicting output

predicted=knn_trained.predict(test_data)

#printing data

print(predicted)
