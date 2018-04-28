# Grace Kelly 25/04/18

# Create scatterplots of Iris data

import matplotlib.pyplot as plt

import numpy

data = numpy.genfromtxt('data/iris.csv', delimiter=',')

petallenght = data[:,0]
petalwidth = data[:,1]

plt.scatter(petallenght,petalwidth)
plt.show()

iris = sns.load_dataset("iris")
iris["ID"] = iris.index
iris["ratio"] = iris["petal_length"]/iris["petal_width"]

sns.lmplot(x="ID", y="ratio", data=iris, hue="species", fit_reg=False, legend=False)

plt.legend()
plt.show()
