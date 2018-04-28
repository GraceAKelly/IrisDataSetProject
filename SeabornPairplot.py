# Grace Kelly #26/04/2018
# https://stackoverflow.com/questions/46383645/seaborn-and-pd-scatter-matrix-plot-color-issues

/import matplotlib.pyplot as plt # import the matplotlib.pyplot library 
import seaborn as sns # advanced graphs library
sns.set(style="ticks", color_codes=True)
iris = sns.load_dataset("iris.csv") # import the iris csv file


iris = sns.load_dataset("iris.csv")
sns.pairplot(iris, hue="species") #create a pairplot

In [3]: run Iris.py # run the script in ipython

In [4]: pl.show() # show the graph visually

  
  
  # Other sources reviewed during research for different approaches
  # https://github.com/mwaskom/seaborn-data
