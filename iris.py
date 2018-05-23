#importing iris dataset from library
from sklearn.datasets import load_iris

#load iris dataset
iris = load_iris()

#separated iris sepal and petal values in dataset

sepal_x = iris.data[0, 0]
sepal_y = iris.data[0, 1]
petal_x = iris.data[0, 2]
petal_y = iris.data[0, 3]

#print dataset in python console
print(iris.data)
