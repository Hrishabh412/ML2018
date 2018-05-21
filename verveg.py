#!usr/bin/python3
import matplotlib.pyplot as plt
import time
from sklearn.datasets import load_iris

#loading iris data

iris=load_iris()

#print flower name

fl_name=iris.target_names
print(fl_name)

#print feature of iris

fl_features=iris.feature_names

print(fl_features)

fl_features_data=iris.data

#loading flower name data

fl_real_data=iris.target

plt.xlabel("versicolor")
plt.ylabel("verginica")
plt.title("IRIS FLOWER")

y1=fl_features_data[50:100]

z1=fl_features_data[100:]
plt.scatter(y1,z1,label="versicolor",marker="x",c='r')

plt.scatter(z1,y1,label="verginica",marker="*",c='b')

plt.legend()
plt.show()


