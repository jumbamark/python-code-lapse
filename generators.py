# Are functions that return traversable objects
""" Writing generators """
def new(dict):
    for x,y in dict.items():
        yield x,y
a={1:"Hi", 2:"Welcome"}
b=new(a)
print(b)
print(next(b))
print(next(b))

""" Example 2 """


def my_func(i):
    while i <= 3:
        yield i
        i += 1


j = my_func(2)  # creating a generator object - j
print(next(j))
print(next(j))

""" Example 2 """
def ex():
    n=3
    yield n
    n=n*n
    yield n
v=ex()
print(next(v))
print(next(v))

""" Generator with loops """
def ex():
    n=3
    yield n
    n=n*n
    yield n
v=ex()
for x in v:
    print(x)

""" Generator expressions """
f=range(6)
print("List comp" ,end=":")   # comprehension
q=[x+2 for x in f]  # storing the values of list comprehension in q
print(q)
print("gen exp" ,end=":")
r=(x+2 for x in f)
print(r)
for x in r:
    print(x)

print("gen exp", end=":")
r = (x + 2 for x in f)
print(r)
print(min(r))

""" Use Cases """
# Fibonacci series - a series of numbers where in each number(fibonacci no.) is a sum of two preceding numbers
def fib():
    f,s=2,3
    while True:
        yield f
        f,s=s,f+s
for x in fib():
    if x>50:
        break
    print(x, end=" ")


# Generating an N length  of fibonacci length  ie Enter the fibonacci length : 8
# [0, 1, 1, 2, 3, 5, 8, 13]
# get a user input for the length of the fibonacci sequence
# set initial values of the sequence
# create a loop and check if the length of the sequence is equal to the number specified .
# If it isn't generate the Fibonacci number and append that to the list of already generated fibonacci numbers
# generate the fibonacci number
inp = int(input("Enter the length of the fibonacci sequence: "))


def fib(fibonacci_length):
    fibonacci_list = [0, 1]
    while len(fibonacci_list) != fibonacci_length:
        second_last_index = len(fibonacci_list) - 2
        last_index = len(fibonacci_list) - 1
        fibonacci_list.append(fibonacci_list[second_last_index] + fibonacci_list[last_index])
    print(fibonacci_list)


fib(inp)


# Number stream - Generating a stream of numbers
a=range(100)
b=(x for x in a) # using a generator expression
print(b)
for y in b:
    print(y)

 # even numbers
a = range(2, 100, 2)  # 2 to 100 in the range of 2
b = (x for x in a)  # using a generator expression
print(b)
for y in b:
     print(y)

# Generating a sine wave using Seaborn-using the normal function(generates all sine waves at once)
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb
def s(flip = 2):
    x = np.linspace(0, 14, 100)
    for i in range(1, 5):
        plt.plot(x,np.sin(x +i * .5) *(7 - i) * flip)

sb.set()
s()
plt.show()

# using the generator function - producing one wave at a time
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
def s(flip = 2):
    x = np.linspace(0, 14, 100)
    for i in range(1, 10):
        yield(plt.plot(x,np.sin(x + i * .5) *(7 - i) * flip))

sb.set()
s=s()
plt.show()
print(next(s))
print(next(s))

