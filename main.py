# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/





import module as md

addition = md.add(10,15)
print(addition)

import sample as s
@do_twice
def say_whee():
    print("Whee!")
say_whee()



# sampler.py reference
from sample import*

print(s.pal("151"))
print(s.fact(5))

@do_twice
def say_whee():
    print("Whee!")


say_whee()

""" Higher order Functions"""


def a_decorator(func):
    def wrapper(*args, **kwargs):
        """A wrapper function"""
        # Extend some capabilities of func
        func()
        func()
    return wrapper


@a_decorator
def first_function():
    """This is docstring for first function"""
    print("This is the first function")


@a_decorator
def second_function():
    """This is docstring for second function"""
    print("second function")


first_function()
print(first_function.__name__)
print(first_function.__doc__)
print(second_function.__name__)
print(second_function.__doc__)

print("First Function")
help(first_function)   # Ideally it should show the name and docstring of wrapped function instead of wrapping function

# Manual solution would be to assign __name__, __doc__ attributes in the wrapping function before returning it.


def a_decorator(func):
    def wrapper(*args, **kwargs):
        """A wrapper function"""
        # Extend some capabilities of func
        func()

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


@a_decorator
def first_function():
    """This is docstring for first function"""
    print("first function")


@a_decorator
def second_function(a):
    """This is docstring for second function"""
    print("second function")


print(first_function.__name__)
print(first_function.__doc__)
print(second_function.__name__)
print(second_function.__doc__)  # If you type help(yourFunction)
# it still has an issue, i.e. the signature of the function, it is showing signature used by wrapper function

# We could use functools.wraps() as decorator to wrapper function as a solution


import functools         # from functools import wraps


def a_decorator(func):
    @functools.wraps(func)         # @wraps(func)
    def wrapper(*args, **kwargs):
        """A wrapper function"""

        # Extend some capabilities of func
        func()

    return wrapper


@a_decorator
def first_function():
    """This is docstring for first function"""
    print("first function")


@a_decorator
def second_function(a):
    """This is docstring for second function"""
    print("second function")


print(first_function.__name__)
print(first_function.__doc__)
print(second_function.__name__)
print(second_function.__doc__)

""" An example on decorators """
# Consider that you have a speak function that returns a neutral message
def speak():
    """Returns a neutral message"""
    return "Hi, Mark!"


# printing the output
print(speak())

# Suppose that you need to modify the function to return a message in a happy tone,so let’s create a decorator for this
def make_mark_happy(func):
    def wrapper():
        neutral_message = func()
        happy_message = neutral_message + " \nYou seem happy!"
        return happy_message
    return wrapper
# using the decorator
@make_mark_happy
def speak():
    return "Hi,Mark"


print(speak())




# globals() in python
# recursive functions
# functools.partial()




""" @property decorator """
# Property function has four arguments: property(fget, fset, fdel,doc)
# fget -retrieves an attribute value
# fset - setting an attribute value
# fdel - deleting an attribute value
# doc - creates a docstring for attribute
# property object has three methods getter(),setter(),delete() to specify fget,fset and fdel individually


# Example
class Geeks:
    def __init__(self):
        self.age = 0

        # function to get value of age
        def get_age(self):
            print("getter method is called")
            return self.age

        # function to set value of age
        def set_age(self,a):
            print("setter method is called")
            self.age = a

        # function to delete age attribute
        def del_age(self):
            del self.age

        age = property(get_age, set_age, del_age)


mark = Geeks()
mark.age = 10
print(mark.age)


# using the @property decorator
class Geeks:
    def __init__(self):
        self._age = 0

    @property
    # getter function
    def age(self):
        return self._age

    # setter function
    def age(self, a):
        if a<18:
            raise ValueError("Sorry,you're a minor")
        else:
            return f"self._age = a"

mark = Geeks()
mark.age = 19
print(mark.age)

# defines properties effortlessly without manually calling the inbuilt function property()
# Property object has three methods: getter(), setter() and delete()
# Example 1 - Defining class
class Portal :
    def __init__(self):
        self.__name = " "

        # using the @property decorator
        @property    # defines property name in class that has three methods: getter, setter and deleter
        # Getter method
        @name.setter
        def name(self):
            return self.__name

        # setter method - sets the value of the attribute
        @name.setter
        def name(self,val):
            self.__name = val

        # Deleter method - deletes the assigned value by the setter method,del invokes deleter
        @name.deleter
        def name(self):
            del self.__name


# Creating an object
p = Portal()

# setting name
p.name = "Jumba Mark"
print(p.name)
del p.name


# Example 2
class Celsius:
    def __init__(self,temp = 0):
        self.temperature = temp

    @property
    # Getter method
    def temp(self):
        print("The value of the assigned temperature is: ")
        return self.temperature

    # setter method
    @temp.setter
    def temp(self,val):
        if val < -273:
            raise ValueError("It is a value error.")
        else:
            print("The value of the temperature is set")
            self.temperature = val


# creating object for stated class
cel = Celsius()
# setting the temperature value
cel.temp = -270
print(cel.temp)

""" @classmethod in python"""
# returns a class method for the given function. Are bound to a class rather than object
class Student:
    # creating a variable
    name = "Elizabeth Keen"

    # creating a function
    def print_name(obj):
        print("The name is: ", obj.name)
# create print_name class method
# IT can be called only with object not with  class
Student.print_name = classmethod(Student.print_name)
Student.print_name()
# used when we want to call many objects with the class name rather than object

# using classmethod() and staticmethod() to check whether a person is an adult or not
from datetime import date

class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        # class method to create a person object by birth year
    @classmethod
    def from_birth_year(cls,name,year):
        return cls(name,date.today().year - year)
    # static method to check if a person is an adult or not
    @staticmethod
    def is_adult(age):
        return age>18
person1 = Person("Shirley",20)
person2 = Person.from_birth_year("Shirley",2005)
print(person1.age)
print(person2.age)
print(Person.is_adult(16))

""" Instance,class and ststic methods - an overview"""
# Everything in python is an object,even classes themselves
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'
# without creating an object instance beforehand
print(MyClass .classmethod())
print(MyClass.classmethod())
print(MyClass.method()) # error because there is no object instance

# creating an object instance
obj = MyClass()
print(obj.method())  # confirmed that the instance method has access to the object instance via the self argument
print(MyClass.method(obj)) # passing the instance method manually
print(obj.classmethod()) # shows it does not have access to the <MyClass instance> object, but only to the <class MyClass> object, representing the class itself
print(obj.staticmethod())

# Examples
class Pizza:
    def __init__(self,ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f"Pizza({self.ingredients!a})"  # 'Pizza(%r)' % self.ingredients
print(Pizza(['cheese', 'tomatoes']))

# incorporating @classmethod

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

# using the cls argument in the margherita and prosciutto factory methods instead of calling the Pizza constructor directly
# They all use the same __init__ constructor internally and simply provide a shortcut for remembering all of the various ingredients.
# Python only allows one __init__ method per class. Using class methods it’s possible to add as many alternative constructors as necessary.
# class methods can’t access the instance (self) but they have access to the class itself via cls.
    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])
print(Pizza.margherita())
print(Pizza.prosciutto())

# When to use static methods
import math
class Pizza:
    def __init__(self,ingredients,radius):
        self.ingredients = ingredients
        self.radius = radius
# modifying the constructor and __rep__ to accept an extra argument
    def __repr__(self):
        return f"Pizza{self.radius!r},{self.ingredients!r}"  # 'Pizza(%r,%s)' % self.ingredients,self.radius

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi
p = Pizza(['mozzarella', 'tomatoes', 'ham'],4)
print(p)
print(p.area())
print(Pizza.circle_area(4))
# static methods can’t access class or instance state because they don’t take a cls or self argument.It's independent of anything else around it











""" String formatting in python """
# Old style
# variables to work with
name = "Bob"
error_no = 50159747054
print("hello, %s"% name)  #  %s tells Python where to substitute the value of name
print('%x' % error_no) # %x format specifier converts an int value to a string and represents it as a hexadecimal number
# making multiple substitutions in a single string;the % operator takes only one argument, you need to wrap the right-hand side in a tuple
print('Hey %s, there is a %x error!' % (name, error_no))
print('Hey %(name)s, there is a %(errno)x error!' % {"name": name, "errno": error_no })

# New style
print('Hello, {}'.format(name))
print( 'Hey {name}, there is a {errno:x} error!'.format(name=name, errno=error_no))

# string interpolation
print(f'Hello, {name}!')
print(f"Hey {name}, there's a {error_no:x} error!")
print(f"Hey {name}, there's a {error_no:#x} error!")
a = 5
b = 10
print(f'Five plus ten is {a + b} and not {2 * (a + b)}.')
def greet(name, question):
    return f"Hello, {name}! How's it {question}?"

print(greet('Bob', 'going'))


# Template strings (standard library)
from string import Template
t = Template('Hey, $name!')
print(t.substitute(name=name))
templ_string = 'Hey $name, there is a $error error!'
print(Template(templ_string).substitute(name=name, error=hex(error_no)))
# the best way to use formatted strings is when you are handling formatted strings generated by users of your program
# it’s possible for format strings to access arbitrary variables in your program;

# this is our super secret key
SECRET = "this-is-a-secret"

class Error:
    def __init__(self):
        pass

# A malicious user can craft a format string that
# can read data from the global namespace:
user_input = '{error.__init__.__globals__[SECRET]}'

# This allows them to exfiltrate sensitive information,
# like the secret key:
err = Error()
print(user_input.format(error = err))

"""JSON data in python"""
# means that script file which is made of  a text in a programming language can be used to and transfer data
import json
a = {"name" : "John","age":31, "salary": 25000}

# conversion to json done by dumps() function
b = json.dumps(a)
print(b)



