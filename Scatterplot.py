# Grace Kelly 22/04/18
# Create scatterplots of Iris data
# https://seaborn.pydata.org/generated/seaborn.pairplot.html
# https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset

import matplotlib.pyplot as plt

import numpy # numerical python library

iris = sns.load_dataset("iris") # load iris.csv to read data in seaborn as a DataFrame
iris["ID"] = iris.index
iris["ratio"] = iris["petal_length"]/iris["petal_width"] # want to display on graph ration petal lenght:width

sns.lmplot(x="ID", y="ratio", data=iris, hue="species", fit_reg=False, legend=False) # label axix and imput data and run scatterplot

plt.legend() # show the legend using matplotlib
plt.show() # show the graph usin matplotlib


iris = sns.load_dataset("iris") # load iris.csv to read data in seaborn as a DataFrame
iris["ID"] = iris.index
iris["ratio"] = iris["sepal_length"]/iris["sepal_width"] # want to display on graph ratio sepal lenght:width

sns.lmplot(x="ID", y="ratio", data=iris, hue="species", fit_reg=False, legend=False) # label axix and imput data and run scatterplot

plt.legend() # show the legend using matplotlib
plt.show() # show the graph usin matplotlib
