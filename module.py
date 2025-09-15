# A file containing a python code,may contain functions,classes etc
""" Creating a module in python """
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def divide(a, b):
    return a / b


""" Built in modules - are written in C and interpreted with using the python interpreter """
from matplotlib import pyplot
print(dir(pyplot))  # The dir func returns an assorted list of strings containing the names defined by a module

import math
print(math.factorial(5))
print(math.sqrt(164))

import random
print(random.randrange(0, 50))

import datetime
print(datetime.datetime.today())

# Demo using the pyplot module in matplotlib
from matplotlib import pyplot as plt

plt.bar([0.25, 1.25, 2.25, 3.25, 4.25],[50, 40, 70, 80, 20], label="BMW", width=.5)
plt.bar([0.75, 1.75, 2.75, 3.75, 4.75],[80, 20, 20, 50, 60], label="Audi",  color="red", width=.5)
plt.legend()
plt.xlabel("Days")
plt.ylabel("Distance (Kms)")
plt.title("Information")
plt.show()

# Piechart
from matplotlib import pyplot as plt
days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]
slices = [7, 2, 2, 13]
activities = ["sleeping", "eating", "working", "playing"]
cols = ["c", "m", "r", "b"]

plt.pie(slices,labels=activities,colors=cols,startangle=90,shadow=True,explode=(0,0.1,0,0),autopct="%1.1f%%")
plt.title("Pie Plot")
plt.show()


# checking for the module we have created
import sample
print(dir(sample))


""" Python module search path - current dir, PYTHONPATH, Default-Dir"""
# when python cannot find the modules in the built-in modules,it searches through the list in the sys.path
import sys
print(sys.path)




