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

plt.xlabel("Setosa")
plt.ylabel("versicolor")
plt.title("IRIS FLOWER")

x1=fl_features_data[0:50]

z1=fl_features_data[50:100]
plt.scatter(x1,z1,label="Setosa",marker="x",c='g')

plt.scatter(z1,x1,label="versicolor",marker="*",c='y')

plt.legend()
plt.show()


