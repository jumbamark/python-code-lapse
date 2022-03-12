
n = int(input("Enter number of rows: "))
for i in range(n):     # number of rows
    for j in range(n-i-1):      # number of spaces in each column
        print(end=" ")       # spaces before star
    for j in range(i+1):    # number of stars in each column
        print("*", end=" ")  # spaces between each star
    print()        # for a new line after finishing the loop per row

# example using a function


def triangle(n):
    k = n - 1      # number of spaces
    # outer loop to handle number of rows
    for i in range(0, n):
        # inner loop to handle number of spaces
        # values changing acc to requirement
        for j in range(0, k):
            print(end=" ")
        # decrementing k after each loop
        k = k - 1
        # inner loop to handle number of columns
        # values changing acc to outer loop
        for j in range(0, i+1):
            print("*", end=" ")
        print()


triangle(5)


# inverse pyramids


def pattern(n):
    k = 2*n - 2
    for i in range (n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


pattern(10)


""" Graph drawing """
from matplotlib import pyplot
years = [1950,1960,1970,1980,1990,2000,2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
# Create a line graph with the x-axis as the year and the y-axis as the gdp
pyplot.plot(years,gdp,c='green',marker='o',linestyle='solid')
# Add a title
pyplot.title( 'Nominal GDP')
# the y axis
pyplot.ylabel('Billion dollar')
# output line diagram
pyplot.show()

""" Depicting a Bar Graph """
# importing modules
import matplotlib.pyplot as plt
import numpy as np

# assigning x and y coordinates
language = ['C','C++','Java','Python']
users = [80,60,130,150]

# depicting the visualization
index = np.arange(len(language))
plt.bar(index,users,color='green')
plt.xlabel('Users')
plt.ylabel( 'language')
plt.xticks(index, language)

# displaying the title
plt.title(label='Number of users of a particular language',fontweight=10,pad='2.0')

""" Depicting a pie chart """
# importing modules
from matplotlib import pyplot as plt
# assigning x and y coordinates
foodPreference = ['Vegeterian', 'Non Vegeterian', 'Vegan', 'Eggitarian']
consumers = [30,100,10,60]

# depicting the visualization
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
ax.pie(consumers, labels=foodPreference, autopct='%1.1f%%')

# displaying the title
plt.title(label="Society Food Preference", loc="left", fontstyle='italic')

""" Showing an image """
# importing modules
from PIL import ImageTk, Image
from matplotlib import pyplot as plt

# depicting the visualization
testImage = Image.open('thread.jpg')

# displaying the title
plt.title("Art",fontsize='30',backgroundcolor='green',color='white')
plt.imshow(testImage)

""" Depicting a RELU function graph """
# importing modules
import matplotlib.pyplot as plt

# assigning x and y coordinates
x = [-5, -4,-3,-2,-1,0,1,2,3,4,5]
y = []

for i in range(len(x)):
    y.append(max(0,x[i]))

# depicting the visualization
plt.plot(x,y, color='green')
plt.xlabel('x')
plt.ylabel ('y')
# depicting the title
plt.title(label="RELU function graph", fontsize=40,color="green")


""" Example on graph plotting """
# Importing relevant modules
import matplotlib.pyplot as plt

# Plotting
x = [1,3,5,10]
plt.plot(x)
plt.show()


""" Example 2"""
import matplotlib.pyplot as plt

# Plotting
x = [1,3,5,10]
y = [7,12,21,22]
plt.plot(x,y)
plt.show()

""" Example 3"""
import matplotlib.pyplot as plt

# Plotting
x =[1,3,5,10]
y = [7,12,21,22]
plt.plot(x, y, c="red",linewidth=3, label= "line 1")
plt.show()


""" Example 4"""
import matplotlib.pyplot as plt

# Plotting
x =[1,3,5,10]
y = [7,12,21,22]
plt.plot(x, y, c="red",linewidth=2, label= "line 1",linestyle = "dashed",marker=("o"),markerfacecolor="black",markersize=10)

# Line 2 - points
x2 = [1,15,18]
y2 = [0,3,12]

# plotting x2 and y2
plt.plot(x2,y2,c="green",linewidth=0.5,label="Line2")

# Label the axes and give the plot a title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Two Lines")

# Show legend on the plot - showing the labels
plt.legend()

# limits of the axes
plt.ylim(0,20)
plt.xlim(0,30)

# Get  pyhton to show the plots
plt.show()