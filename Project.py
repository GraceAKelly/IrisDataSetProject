# Grace Kelly 28/04/2019
# Attribute heading to columns within Iris Data Set
# https://docs.python.org/3.1/library/csv.html
# https://github.com/venky14/Machine-Learning-with-Iris-Dataset/blob/master/Machine%20Learning%20with%20Iris%20Dataset.ipynb

import numpy as np  # import numnerical python with shorthand  
import matplotlib.pyplot as pl  # shorthand import for matplotlib library
import seaborn as sns # import seaborn for advanced graphics
import pandas as pd # import pandas for to take data from table in ncsv file
import csv

iris = pd.read_csv('data/iris.csv', delimiter=',', names=['Sepal Lenght', 'Sepal Width', 'Petal Lenght','Petal Width','Class']) 
# read iris.csv file using pandas and attribute heading to columns

In [13]: run Project.py # use ipython to run script

In [14]: iris.head() # prints the first five rows with given headings 
Out[14]:
   Sepal Lenght  Sepal Width  Petal Lenght  Petal Width        Class
0           5.1          3.5           1.4          0.2  Iris-setosa
1           4.9          3.0           1.4          0.2  Iris-setosa
2           4.7          3.2           1.3          0.2  Iris-setosa
3           4.6          3.1           1.5          0.2  Iris-setosa
4           5.0          3.6           1.4          0.2  Iris-setosa

In [16]: iris.info() # output basic information using pandas on the csv file already run giving the number of rows and columns
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
Sepal Lenght    150 non-null float64
Sepal Width     150 non-null float64
Petal Lenght    150 non-null float64
Petal Width     150 non-null float64
Class           150 non-null object
dtypes: float64(4), object(1)
memory usage: 5.9+ KB

# Create Histogram https://github.com/venky14/Machine-Learning-with-Iris-Dataset/blob/master/Machine%20Learning%20with%20Iris%20Dataset.ipynb
# Indicating colour of the bar chart edging and line width
In [17]: iris.hist(edgecolor='black', linewidth=1.2)
    ...: fig = pl.gcf()
    ...: fig.set_size_inches(12,6)
    ...: pl.show() # shorthand to show the graph 

# Create Boxplots 
In [22]: iris.boxplot() # code to create boxplots in pandas
Out[22]: <matplotlib.axes._subplots.AxesSubplot at 0x2610c8d4e10>

In [23]: pl.show() # show the graph boxplot
QWindowsWindow::setGeometry: Unable to set geometry 1500xQWindowsW
