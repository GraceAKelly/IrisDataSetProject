IrisDataSetProject
==========================================================
Background
----------------------------------------------------------
The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.(https://en.wikipedia.org/wiki/Iris_flower_data_set)

![Ronald Fisher](R._A._Fischer.jpg)

Originally published at UCI Machine Learning Repository: Iris Data Set, is often used for testing out machine learning algorithms and visualizations (for example, Scatter Plot). Each row of the table represents an iris flower, including its species and dimensions of its botanical parts, sepal and petal, in centimeters.(https://gist.github.com/curran/a08a1080b88344b0c8a7)

For project analysis the data set was imported to visual studio code as a csv file from [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris)

The 5 columns within the file were attributed relevant column headings - Sepal Length, Sepal Width, Petal Length, Petal Width and Class as per [The Python Tutorial](https://docs.python.org/3.1/library/csv.html)

The dataset contains a set of 150 records under 5 attributes 
[NumPy](https://en.wikipedia.org/wiki/NumPy)is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

[IPython](https://en.wikipedia.org/wiki/IPython) is a command shell for interactive computing in multiple programming languages, originally developed for the Python programming language, that offers introspection, rich media, shell syntax, tab completion, and history.

Creating Histograms
[Histograms](https://matplotlib.org/gallery/statistics/histogram_features.html)


![Petal Lenght Histogram](PetalLenghtHistogram.png)
![Petal Width Histogram](PetalWidthHistogram.png)
![Sepal Lenght Histogram](SepalLenghtHistogram.png)
![Sepal Width Histogram](SepalWidthHistogram.png)


Creating boxplots
[Boxplots](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.boxplot.html)

Scatter plots were created to display the correlation between petal lenght and petal width for the three different class types. [Reference source](https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset)


![Ratio of Petal Lenght:Petal Width per class](Scatterplot_Ratio_Petal_Lenght_vs_Petal_Width.png)

![Ratio of Sepal Lenght:Sepal Width per class](Scatterplot_Sepal_Lenght_vs_Sepal_Width.png)

[Seaborn](https://stackoverflow.com/questions/46383645/seaborn-and-pd-scatter-matrix-plot-color-issues)
![Seaborn Pairplot](SeabornPairPlot.png)


