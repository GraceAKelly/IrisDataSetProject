# Grace Kelly 17/04/18

# Calculate the mean, minimum maximum and standard deviation of each column in Iris data set

import numpy # numerical python library

data = numpy.genfromtxt('data/iris.csv', delimiter=',') # set delimiter in file as comma

sepallenght = data[:,0] # define sepal lenght as data in the first column
meansepallenght = numpy.mean(data[:,0]) # use numpy library to calculate mean of first column
print("Average of the sepal lenght is: ", meansepallenght) # output mean of first column

sepalwidth = data[:,1] # define sepal width as data in the second column
meansepalwidth = numpy.mean(data[:,1]) # use numpy library to calculate mean of second column
print("Average of the sepal width is: ", meansepalwidth) # output mean of first column

petallenght = data[:,2] # define petal lenght as data in the third column
meanpetallenght = numpy.mean(data[:,2])# use numpy library to calculate mean of third column
print("Average of the petal lenght is: ", meanpetallenght) # output mean of third column

petalwidth = data[:,3] # define petal width as data in the fourth column
meanpetalwidth = numpy.mean(data[:,3])# use numpy library to calculate mean of fourth column
print("Average of the petal width is: ", meanpetalwidth) # output mean of fourth column

In [24]: run Irisdataset.py #test data
Average of the sepal lenght is:  5.84333333333
Average of the sepal width is:  3.054
Average of the petal lenght is:  3.75866666667
Average of the petal width is:  1.19866666667

# Using ipython caculate the min and max for sepal lenght

In [40]: sepallenght.min()
Out[40]: 4.2999999999999998

In [41]: sepallenght.max()
Out[41]: 7.9000000000000004

# Using ipython caculate the min and max for sepal width
In [42]: sepalwidth.min()
Out[42]: 2.0

In [43]: sepalwidth.max()
Out[43]: 4.4000000000000004

# Using ipython caculate the min and max for petal lenght
In [44]: petallenght.min()
Out[44]: 1.0

In [45]: petallenght.max()
Out[45]: 6.9000000000000004

# Using ipython caculate the min and max for petal width
In [46]: petalwidth.min()
Out[46]: 0.10000000000000001

In [47]: petalwidth.max()
Out[47]: 2.5

# Using ipython caculate the standard deviation of sepal lenght
In [48]: sepallenght.std()
Out[48]: 0.82530129178514089

# Using ipython caculate the standard deviation of sepal width
In [49]: sepalwidth.std()
Out[49]: 0.43214658007054352

# Using ipython caculate the standard deviation of petal lenght
In [50]: petallenght.std()
Out[50]: 1.7585291834055212

# Using ipython caculate the standard deviation of petal width
In [52]: petalwidth.std()
Out[52]: 0.76061261858817164
