import numpy as np 
import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
print(type(iris))

print(iris.keys())

print(iris['data'])

X_train, X_test, Y_train, Y_test = train_test_split(iris['data'],iris['target'])

knn = KNeighborsClassifier(n_neighbors=25)
knn.fit(X_train, Y_train)

print(knn)

a = knn.score(X_test,Y_test)
print(a)