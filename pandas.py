# python applications
# Data analysis - to perform data analysis you need to import pandas
# pandas is a software library used for data manipulation and data analysis
# build on numpy, scipy and matplotlib(data visualization module)

# how to create a data frame
import pandas as pd
# defining a dictionary that contains data about some website
# bounce rate is the number of people who have visited you web but have left immediately
XYZ_web = {"Day":[1,2,3,4,5,6], "Visitors":[1000,700,6000,1000,400,350], "Bounce_Rate":[20,20,23,15,10,34]}
# converting the dictionary into a pandas data frame
df = pd.DataFrame(XYZ_web)
print(df)

""" Pandas operations """
""" slicing the data frame"""
print(df.head(2))
print(df.tail(3))

"""joining and merging"""
# merging
import pandas as pd
df1 = pd.DataFrame({"HPI": [80,90,70,60],"Int_rate": [2, 1, 2, 3],"IND_GDP": [50,45,45,67]}, index=[2001,2002,2003,2004])
print(df1)

# defining three data frames
# opening the first dict ,closing it and defining index values
df1 = pd.DataFrame({"HPI": [80,90,70,60],"Int_rate": [2, 1, 2, 3],"IND_GDP": [50,45,45,67]}, index=[2001,2002,2003,2004])
df2 = pd.DataFrame({"HPI": [80,90,70,60],"Int_rate": [2, 1, 2, 3],"IND_GDP": [50,45,45,67]}, index=[2005,2006,2007,2008])
merge = pd.merge(df1, df2)
print(merge)

# keeping a particular column common
merge = pd.merge(df1, df2, on="HPI")
print(merge)

# joining
import pandas as pd
df1 = pd.DataFrame({"Low_tier_HPI": [50,45,45,67], "unemployment":[1,3,5,6]}, index=[2001,2002,2003,2004])
df2 = pd.DataFrame({"Int_rate": [2, 1, 2, 3],"IND_GDP": [50,45,45,67]}, index=[2001,2003,2004,2004])
joined = df1.join(df2)
print(joined)

"""changing the index and column headers"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")
df = pd.DataFrame({"Day":[1,2,3,4], "Visitors": [200,100,230,300], "Bounce_rate":[20,45,60,10]})
print(df)

# changing day to be index values
df.set_index("Day", inplace=True)
print(df)
df.plot()
plt.show()

# converting one of the column headers(from visitors to users)
df = df.rename(columns={"Visitors": "users"})
print(df)

"""concatenation"""
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.DataFrame({"HPI": [80, 85, 88, 85],
                    "Int_rate": [2, 3, 3, 2],
                    "US_GDP_Thousands": [50, 55, 65, 55]},
                   index=[2001, 2002, 2003, 2004])
df2 = pd.DataFrame({"HPI": [80, 85, 88, 85],
                    "Int_rate": [2, 3, 3, 2],
                    "US_GDP_Thousands": [50, 55, 65, 55]},
                   index=[2005, 2006, 2007, 2008])

concat = pd.concat([df1, df2])
print(concat)
concat.plot()
plt.show()

"""data munging - convert a particular format of data into a different format; i.e csv into html"""
import pandas as pd
# reading a file present in the system
# index_col=0,makes sure that no index present in that data frame
country = pd.read_csv("/home/mark/Downloads/API_ILO_country_YU.csv", index_col=0)
country.to_html("stats.html")

# Use case
# Problem Statement - find the percentage change of unemployed youth for every country from 2010-2011
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")
country = pd.read_csv("/home/mark/Downloads/API_ILO_country_YU.csv", index_col=0)
df = country.head(5)
df = df.set_index(["Country Code"])
sd = df.reindex(columns=["2010","2011"])  # only 2010 and 2011 to be columns
print(sd)
db = sd.diff(axis=1) # defining one more data frame - difference between the two columns
db.plot(kind="bar")
plt.show()


""" Python for statistics """
# Mean
from statistics import mean, median, mode, variance
print(mean([101, 334, 65, 35, 56, 78, 65, 86]))
print(median([1, 1, 1, 2, 2]))
print(mode([1, 1, 1, 2, 2]))
print(variance([101, 334, 65, 35, 56, 78, 65, 86]))

""" python for hadoop: pydoop """
# pydoop is a python interface that allows you to write Mapreduce apps and interact with HDFS in pure python

"""Matplotlib"""
# Data visualization - presentation of data in a pictorial or graphical format
# Basic example
from matplotlib import pyplot as plt
plt.plot([1, 2, 3], [4, 5, 1])
plt.show()

# Naming the axes and title
import matplotlib.pyplot as plt
x = [5, 8, 10]
y = [12, 16, 6]

plt.plot(x, y)
plt.title("info")
plt.ylabel("Y axis")
plt.xlabel("X axis")
plt.show()

# how to add style to your graph
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
x = [5, 8, 10]
y = [12, 16, 6]

x2 = [6, 9, 11]
y2 = [6, 15, 17]

plt.plot(x, y, "g", label="line one", linewidth=5)
plt.plot(x2, y2, "y", label="line two", linewidth=5)

plt.title(" Epic Info")
plt.xlabel("X axis")
plt.ylabel("y axis")
plt.legend()
plt.grid(True, color="k")
plt.show()

# How to plot bar graph - comparison between groups
import matplotlib.pyplot as plt
plt.bar([1, 3, 5, 7, 9], [5, 2, 7, 8, 9], label="Example One", color="blue")
plt.bar([2, 4, 6, 8, 10], [8, 6, 2, 5, 6], label="Example 2", color="red")
plt.legend()
plt.title("Bar Graph")
plt.xlabel("Bar Number")
plt.ylabel("Bar Height")
plt.show()

# Histogram
import matplotlib.pyplot as plt
population_ages = [4, 10, 23, 45, 68, 4, 77, 89, 21, 56, 90, 14, 33, 94, 130, 112, 114, 140, 150, 88, 66, 2, 9, 19, 20]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_ages, bins, histtype="bar", rwidth=0.8)
plt.title("Histogram")
plt.xlabel("Age")
plt.ylabel("Frequencies")
plt.show()

# Scatter plot
# used when comparing 2 variables or three if you are plotting in three dimension looking for a co-relation of groups
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 2, 1, 4, 5, 2]

plt.scatter(x, y, label="skitscat", color="k")
plt.xlabel("x")
plt.ylabel("Y")
plt.title("Scatter plot")
plt.legend()
plt.show()

# Area/stack plot
# can be used to track changes over time for one or more groups
# are good to use when tracking the changes between two or more related groups that make up one whole category
import matplotlib.pyplot as plt
days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

plt.plot([], [], color="m", label="sleeping", linewidth=5)
plt.plot([], [], color="c", label="eating", linewidth=5)
plt.plot([], [], color="r", label="working", linewidth=5)
plt.plot([], [], color="k", label="playing", linewidth=5)

plt.stackplot(days, sleeping, eating, working, playing, colors=["m", "c", "r", "k"])
plt.xlabel("Days")
plt.ylabel("Activities")
plt.title("Stack Plot")
plt.legend()
plt.show()

# Pie Chart
import matplotlib.pyplot as plt
slices = [2, 2, 13, 7]
activities = ["sleeping", "eating", "playing", "working"]
cols = ["c", "r", "m", "b"]
plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0, 0.1, 0, 0),
        autopct="%1.1f%%")
plt.title("Pie PLot")
plt.show()

""" Sub plot - helps to plot multiple plots"""
import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)


t1 = np.arange(0.0, 5.0, 0.1)  # create es a np array that will have elements between 0 to 5 in the steps of .1
t2 = np.arange(0.0, 5.0, 0.02)

# we have 2 plots, horizontally we have one plot present and  vertically we have two plots
# and in the vertical position these plot will be our first graph
plt.subplot(211)
plt.plot(t1, f(t1), "bo", t2, f(t2))

# vertically we have two plots , horizontally we have one and these is the second plot
plt.subplot(212)
plt.plot(t2, np.cos(2 * np.pi * t2))
plt.show()

# changing the plot to see what we get - we gwt the same graph but it is aligned horizontally
import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)


t1 = np.arange(0.0, 5.0, 0.1)  # create es a np array that will have elements between 0 to 5 in the steps of .1
t2 = np.arange(0.0, 5.0, 0.02)

# we have 2 plots, horizontally we have one plot present and  vertically we have two plots
# and in the vertical position these plot will be our first graph
plt.subplot(221)
plt.plot(t1, f(t1), "bo", t2, f(t2))

# vertically we have two plots , horizontally we have one and these is the second plot
plt.subplot(222)
plt.plot(t2, np.cos(2 * np.pi * t2))
plt.show()


""" Seaborn """
# it is a data visualization library available in python,based on matplotlib and allows creation of statistical graphics
# alllows comparison of multiple variables , supports multiple plot grids, has color pellets
# estimates plot linear regression vertically,
# seaborn vs matplotlib - matplotlib settings are difficult to figure out
# matplotlib does not serve well when it comes to data frames, seaborn functions work on data frames

""" Seaborn functions """
# visualizing statistical relationships - understanding relationships between variables of a data set
import seaborn as sb

# you can load any data set present on github and make use of it with seaborn
# seaborn allows you to  load any data set present on git using the load dataset function
a = sb.load_dataset("flights")   # loading the flight data set function
sb.relplot(x="passengers", y="month", data=a)  # a is the variable where am loading the data set

# the previous points are plotted in two dimensions, adding another dimension
import numpy as np
import seaborn as sb

a = sb.load_dataset("flights")
sb.relplot(x="passengers", y="month", hue="year", data=a)

# line plot (previous one is a scatter plot)
import seaborn as sb
b = sb.load_dataset("tips")
sb.relplot(x="time", y="tip", data=b, kind="line")


# plotting with categorical data - main variable is further divided into discrete groups
import seaborn as sb
b = sb.load_dataset("tips")
sb.catplot(x="day", y="total_bill", data=b)

# scatter plot is the default type of  catplot however you can change the type of plot you want
import seaborn as sb
b = sb.load_dataset("tips")
sb.catplot(x="day", y="total_bill", kind="violin", data=b)  # try boxen as your kind


# visualizing the distribution of a data set - understanding data sets with context to being uni-variate or bi-variate
# example of a uni-variate distribution
import numpy as np
c = np.random.normal(loc=5, size=100, scale=2)
sb.distplot(c)

# plotting a bi-variate distribution
import seaborn as sb
import pandas as pd
import numpy as np
x = pd.DataFrame({"Day": [1, 2, 3, 4, 5, 6, 7],
                  "Grocery": [30, 80, 45, 23, 51, 46, 76],
                  "Clothes": [13, 40, 34, 23, 54, 67, 98],
                  "utensils": [12, 32, 27, 24, 40, 61, 59]})

y = pd.DataFrame({"Day": [8, 9, 10, 11, 12, 13, 14],
                  "Grocery": [30, 80, 45, 23, 51, 46, 76],
                  "Clothes": [13, 40, 34, 23, 54, 67, 98],
                  "utensils": [12, 32, 27, 24, 40, 61, 59]})

mean, cov = [0, 1], [(1, .5), (.5, 1)]
data = np.random.multivariate_normal(mean, cov, 200)
with sb.axes_style("white"):
    sb.jointplot(x=x, y=y, kind="kde", color="b")


""" Multi-plot grids"""
# graphs are plotted side by side using the same scale and axes to aid in comparison
import seaborn as sb
import matplotlib.pyplot as plt
a = sb.load_dataset("iris")
b = sb.FacetGrid(a, col="species")
b.map(plt.hist, "sepal_length")

# Pair gid function - when you have a pair of functions to compare
import seaborn as sb
import matplotlib.pyplot as plt
a = sb.load_dataset("flights")
b = sb.PairGrid(a)
b.map(plt.scatter)

""" Plot Aesthetics """
# deals with making plots more attractive and delightful using various themes and color pellets
import seaborn as sb
sb.set(style="darkgrid")
import matplotlib.pyplot as plt
a = sb.load_dataset("flights")
b = sb.PairGrid(a)
b.map(plt.scatter)

# Example 2
import seaborn as sb
sb.set(style="white", color_codes=True)
a = sb.load_dataset("tips")
sb.boxenplot(x="day", y="total_bill", data=a)  # plot will have axes around it

# removing the axes
import seaborn as sb
sb.set(style="white", color_codes=True)
a = sb.load_dataset("tips")
sb.boxenplot(x="day", y="total_bill", data=a)  # plot will have axes around it
sb.despine(offset=10, trim=True)

# color palettes available in seaborn
import seaborn as sb
c = sb.color_palette()
sb.palplot(c)


""" FIFA use case - data science """
# predicting  the world's best playing 11 - goalkeeper, 4 defenders, 3 midfielders and 3 attackers
# collect and analyze FIFA Dataset
import pandas as pd
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("/home/mark/Downloads/players_21.csv")
del df["body_type"]   # deletes the column body type
print(df.head(7))

# doing analysis of players from their countries
plt.figure(figsize=(60, 80))
sb.countplot(y=df.nationality, palette="Set2")  # plots all the nations on the y axis

# Doing an analysis on age
plt.figure(figsize=(15, 6))
sb.countplot(x="age", data=df)

# Assignment
# Best goalkeeper
# assigning weights
a = 0.5
b = 1
c = 2
d = 3

# goalkeeping characteristics
# in order to find the best goalkeeper we are analysing the data for the two parameters
df["goalkeeping_positioning"] = (d*df.mentality_aggression + c*df.mentality_vision + b*df.goalkeeping_diving + a*df.defending_sliding_tackle)
df["goalkeeping_handling"] = (d*df.mentality_composure + c*df.skill_long_passing + b*df.power_jumping)

plt.figure(figsize=(15, 6))

# Generating sequential data and plot
sd1 = df.sort_values("goalkeeping_handling", ascending=False)[:5]
x1 = np.array(list(sd1["Name"]))
y1 = np.array(list(sd1["goalkeeping_handling"]))

sb.barplot(x1, y1, palette="colorblind")
plt.ylabel("Goal Keeper Handling Score")

# plot goalkeeping positioning
plt.figure(figsize=(15, 6))

sd = df.sort_values("goalkeeping_positioning", ascending=False)[:5]
x2 = np.array(list(sd["Name"]))
y2 = np.array(list(sd["goalkeeping_positioning"]))
sb.barplot(x2, y2, palette="colorblind")
plt.ylabel("Positioning Score")

# choosing defenders
df["lb"] = (d*df.physic + d*df.defending)
df["rb"] = (d*df.passing + b*df.defending + a*df.dribbling)

# plot left back
plt.figure(figsize=(15, 6))
sd = df[(df["team_position"] == "LB")].sort_values("lb", ascending=False)[:5]
x2 = np.array(list(sd["Name"]))
y2 = np.array(list(sd["lb"]))
sb.barplot(x2, y2, palette=sb.color_palette("Blues_d"))
plt.ylabel(" Left Back Score")    # continue with the same process
