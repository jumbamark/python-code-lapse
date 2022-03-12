x = 10
y = 12
print(y % x)

# Data types
# Numbers
# integer: x = 10
# float: x = 10.234
# complex = 25j

# String
x = "of"
y = "a"
z = input()
print("Here is an example", x, y, z)

name = "Mark"
print(len(name))

# index numbers - they start from zero
print(name[2])  # accessing a value from the string using index numbers
# strings are immutable, yo can not change them
# name[2] = "d"  # raises an error
print(name[1:8])  # accessing a series of letters from a string
print(name.upper())   # changing all the letters to upper case

# List data type
# a list is a collection of arrays which is changeable and ordered, they have indexes
Fruits = ["apple", "kiwi", "mango", "banana"]   # we use square brackets to declare a list
my_list = [10, 40, "apple"]
print(my_list)
print(*my_list)  # unpacking
my_list[2] = 30  # replaces apple with 30
print(my_list)
my_list.append(50)    # # adds 50 to the end of the list
print(my_list)
my_list.insert(1, "apple")  # adding a string at the index 1
print(my_list)
my_list.reverse()   # reverses the list
print(my_list)

# Dictionary
# is a collection like a list but it is un-ordered changeable and indexed
my_dict = {"reptiles": "snake",
           "mammals": "whale",
           "amphibians": "frogs",
           1: "python",
           2: "data science"}
print(my_dict)

print(my_dict[2])
my_dict[1] = "machine learning"      # updating a value
my_dict[3] = " web development"  # adding a value
print(my_dict)

# Tuple
# it is immutable
animals = (10, 20, 20, 30, "tiger", "lion")
print(animals[3])

# set
# duplicate values and does not support indexing
my_set = {20, 20}
print(my_set)

a = [2, 3, 4, 5]
b = {6, 7, 8, 9}
c = [*a, *b]
print(c)


# collections in python - lists, sets, tuples and dictionaries
from collections import namedtuple
a = namedtuple("courses", "name, technology")
s = a("data science", "python")
print(s)


# Arrays
# it is a data structure with ordered series of elements
# arrays store only single data types but lists can have any data
from array import*
a = array("i", [1, 2, 3, 4, 5])    # array constructor, type code, value list
print(a)
print(a[0])

# finding the length of an array
a = array("i", [1, 2, 3, 4, 5])
print(len(a))

# adding elements
a.append(6)  # add one element at the end of the array
print(a)
a.extend([7, 8, 9])  # adds more than one element
print(a)
a.insert(2, 200)    # adds at a specific position
print(a)

# removing elements
a = array("i", [1, 2, 3, 4, 5])
print(a.pop())  # removes last element unless specified and returns the element
a.remove(3)  # removes the specified element
print(a)

# array concatenation/ joining
a = array("i", [1, 2, 3, 4, 5])
b = array("i", [6, 7, 8, 9, 10])
c = a + b
print(c)


# slicing an array
a = array("i", [1, 2, 3, 4, 5])
print(a[0:3])

# Looping through an array
# for - iterates for a specified number of times
# while - iterates until some condition is met (initialize iterator, specify a condition, increment iterator)
a = array("i", [1, 2, 3, 4, 5])
for x in a[0:3]:
    print(x)

# while loop
a = array("i", [1, 2, 3, 4, 5])
temp = 0
while temp < a[2]:
    print(a[temp])
    temp += 1

# Hash tables/maps
# type of data structure which maps keys to it's value pairs
# creating dictionaries - using curly braces or using dict() function
my_dict={"Dave": "001", "Ava": "002", "Joe": "003"}
print(my_dict)

new_dict = dict(Dave="001", Ava="002", Joe="003")
print(new_dict)

# Nested dictionaries
emp_details = {"Employees": {"Dave": {"ID": "001", "salary": "2000", "Designation": "Team Lead"},
                            "Eva": {"ID": "002", "salary": "1000", "Designation": "Associate"}}}
print(emp_details)
print(emp_details["Employee"])

# Accessing values in dict
my_dict = {"Dave": "001", "Ava": "002", "Joe": "003"}
print(my_dict.keys())  # all  keys present in my dict
print(my_dict.values())
print(my_dict.get("Ava"))

# getting keys using for loop
for x in my_dict:
    print(x)

# getting values using for loop
for x in my_dict.values():
    print(x)

# getting all key value pairs
my_dict = {"Dave": "001", "Ava": "002", "Joe": "003"}
for x, y in my_dict.items():
    print(x, y)

# Updating values in a dictionary
my_dict = dict(Dave="001", Ava="002", Joe="003")
my_dict["Dave"] = "004"
my_dict["Chris"] = "001"
print(my_dict)

# Deleting functions
del my_dict["Dave"]
print(my_dict)

# Converting a dictionary into a data frame
import pandas as pd
emp_details = {"Employees": {"Dave": {"ID": "001", "salary": "2000", "Designation": "Team Lead"},
                            "Eva": {"ID": "002", "salary": "1000", "Designation": "Associate"}}}
df = pd.DataFrame(emp_details["Employees"])
print(df)

# Operators in python
x = 10
y = 20
print(x+y)
print(x**y)    # exponentiation
print(x % y)    # gives the value that is a reminder

# Assignment operators
a = 20
a += 5  # add 5 to a and return the value as a
print(a)

# conditional statements
val = 10
num1 = 20
if val == num1:
    print("equal")
elif val != num1:
    print("not equal")
else:
    print("nothing")

# logical operators - are used to combine conditional statements
x = 10
print(x > 8 and x > 5)
print(x > 8 or x > 14)
print(not(x > 8 and x > 5))

# identity operators
list1 = [10, 20, 30]
list2 = [10, 20, 30]
x = list1
print(x is list1)
print(list1 is list2)
print(list1 is not list2)

































