""" Lambda """  # Python lambda functions are anonymous or nameless functions, lambda is keyword and not a name.
# How to write anonymous functions.
# Lambda arguments:expression
lambda a: a*a
x =lambda a: a*a
print(x(3))

""" normal line of code """


def new(a):
    return a*a


print(new(3))

""" Anonymous functions within user defined functions """


def new_func(x):
    return lambda y: x+y

t = new_func(3)
u = new_func(2)
print(t(6))
print(u(3))

"""Lambda within anonymous functions - Example 2"""
def A(x):
    return lambda y: x+y
t = A(4)  # Giving a value to the variable x and storing in another variable t
print(t(10))   # Printing a value of x+y
u=A(7)
print(u(5))

""" Using Lambda Functions within filter(), map() and reduce() functions"""
# Lambda within Filter() - used to filter the given iterables(lists,sets) -to test all elements to be true or false
my_list=[2,3,4,5,6,7,8]
new_list=list(filter(lambda a:(a/3 ==2),my_list)) # SYNTAX: filter(function,iterables)
print(new_list)

# Lambda within Map() - Applies a given function to all the iterables and returns a new lists.
my_list=[2,3,4,5,6,7,8]
new_list=list(map(lambda a:(a/3!=2),my_list))
print(new_list)

# Lambda within reduce  - applies some other functions to the sequence and returns a single value
from functools import reduce # import functools or from functools import *
p=reduce(lambda a,b: a+b, [23,56,43,98,1])    # SYNTAX: reduce(function,sequence)
print(p)

""" Solving Algebraic equations using lambda """
# Linear Equations
s = lambda a:a*a
s(4)
print(s(4))

# 3x+4y
d = lambda x,y: 3*x + 4*y
a=d(4,7)
print(a)

# Quadratic Equation - (a+b)^2
x=lambda a,b: (a+b)**2
c=x(3,4)
print(c)

""" Map-Reduce Functions """
# Map Function
def new(a):
    return a*a
x = map(new, [1,2,3,4])
print(x)
print(list(x))

# Example 2
def new(a,b):
    return a*b
x = map(new, [1,2,3,4],[2,3,4,5])
print(x)
print(list(x))

# Using lambda functions along with map functions
lst=[1,2,3,4,5]
y=list(map(lambda x: x+3,lst))
print(y)

# Filter Functions - SYNTAX : filter(function,iterables)
def new1(i):
    if i>=3:
        return i
j=filter(new1,(1,2,3,4,5,6,7))
print(j)
print(tuple(j))

# Using filter function along with lambda function
z = filter(lambda x: (x>=3),(1,2,3,4,5,6,7,8))
print(list(z))

# Reduce Function
from functools import reduce
def a(x,y):
    return x+y
s=reduce (a,[1,2,3,4,5,6,7,8,8])
print(s)

# Using reduce functions with lambda functions
b=reduce(lambda q,p: q*p,[1,2,3,45,6,7,7])
print(b)

# Filter within map
c=map(lambda x:x+x,filter(lambda x:(x>=4),[2,3,4,5]))
print(tuple(c))

# Map Function within the filter function
d=filter(lambda x:(x>=4),map(lambda x:x+x,[2,4,6,8,10]))
print(set(d))

# Map and Filter within Reduce
r=reduce(lambda x,y:x+y, map(lambda x:x+x, filter(lambda x: (x>=4),[1,2,3,4,5,6])))
print(r)