""" How we use the first class object """
def func1(name):
    return f"Hello{name}"


def func2(name):
    return f"Hello{name} , how you doing?"


def func3(func4):
    return func4('Dear learner')


print(func3(func1))
print(func3(func2))

""" How we use inner functions """
def func():
    print("first function")
    def func1() :
        print("first child function")
    def func2() :
        print("second child function")

    func2 ()
    func1 ()

func()

""" returning a function from a function - taking a function as an argument for another function """
def func (n):
    def func1 ():
        return "edureka"
    def func2 ():
        return "python"
    if n == 1:
        return func1
    else:
        return func2
a = func(1)
b = func(2)
print (a())
print (b())

""" Decorators in pyhton """
def function1(function):
     def wrapper ():
         print("hello")
         function()
         print("welcome to pyhton edureka tutorial")
         return wrapper

def function2():
    print ("pyhtonista")

function2 = function1(function2)

function2()

""" specifying a decorator with arguments in a program """
def function1(function) :
    def wrapper (*args, **kwargs) :
        print("hello")
        function(*args, **kwargs)
        print("welcome to edureka python tutorial")
    return wrapper

@function1
def function2(name):
    print(f"{name}")

function2("waseem")

""" Example 2 """
def function1(function):
    def wrapper(*args, **kwargs) :
        print("it worked")
        function(*args, **kwargs)
    return wrapper

@function1
def function2(name) :
    print(f"{name}")

function2("python")

""" Fancy Decorators -class decorators """
class square:
    def __init__(self,side):
        self._side = side
    @property
    def side(self):
        return self._side
    @side.setter
    def side(self,value):
        if value >= 0:
            self.side = value
        else:
            print("error")
    @property
    def area(self):
        return self._side **2
    @classmethod
    def unit_square(cls):
        return  cls(1)
s = square(5)
print(s.side)
print(s.area)

"""" Fancy Decorators - making a singleton class using class decorators"""
import functools
def singleton(cls):
    @functools.wraps(cls)
    def wrapper(*args,**kwargs):
        if not wrapper.instance:
            wrapper.instance = cls(*args, *kwargs)
        return wrapper.instance
    wrapper.instance = None
    return wrapper

@singleton
class one:
    pass

first = one()
second = one()

print(first is second)

""" Nested Decorators in a Function"""
import functools

def repeat(num):
    def decorator_repeat (func) :
        @functools.wraps(func)
        def wrapper(*args, **kwargs) :
            for _ in range(num):
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator_repeat

@repeat(num = 5)
def function(name):
    print (f"{name}")

function("python")





""" Decorator and first class functions(rough work)"""
# functions
def add_one(number):
    return number + 1


add_one(2)
print(add_one(2))

# first class objects
def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

print(greet_bob(say_hello))
print(greet_bob(be_awesome))

# inner functions
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

print(parent())


# returning functions from functions
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child
first = parent(1)
second = parent(2)
print(first)
print(first())

# simple decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)
say_whee()

# Example 2
# So as not to disturb your neighbors, the following example will only run the decorated code during the day
from datetime import datetime


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")  #    If you try to call say_whee() after bedtime, nothing will happen



say_whee = not_during_the_night(say_whee)
print(say_whee())


# syntactic sugar -  using decorators in a simpler way with the @ symbol
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator  # Easier way of saying say_whee = my_decorator(say_whee).
def say_whee():
    print("Whee!")
(say_whee())

# Reusing decorators
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice
@do_twice
def func():         #can use any name apart from func
    print("I am Mark")
func()
#You can now use this new decorator in other files by doing a regular import-refer to main.py

# Decorating functions with arguments
from sample import do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")
greet("world")  # returns an error since wrapper_do_twice takes no positional argument but name="world" was given
# The solution is to use *args and **kwargs in the inner wrapper function,it will accept an arbitrary number of positional and keyword arguments

# Returning values from decorated functions
from sample import do_twice


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

return_greeting("Keen")
#Because the do_twice_wrapper() does not explicitly return a value, the call return_greeting("Adam") ended up returning None.

# To fix this, you need to make sure the wrapper function returns the return value of the decorated function.
from decorator import do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

print(return_greeting("Tom Keen"))

"""Code introspection in Python"""
# the type function returns the type of object
import math
print(type(math))
print(type(2))
print(type("I"))
rk = [1, 2, 3, 4, 5, "radha"]

print(type(rk))
print(type(rk[1]))
print(type(rk[5]))

# the dir functions returns the list of methods and attributes associated with that object
import math
rk = [1, 2, 3, 4, 5]

# print methods and attributes of rk and math
print(dir(rk))
print(dir(math))

# the string function converts everything into a string
a = 1
print(type(a))

# converting integer into a string
a = str(a)
print(type(a))

s = [1, 2, 3, 4, 5]
print(type(s))

# converting list into a string
s = str(s)
print(type(s))

# id() function returns a special id of an object
import math
b = (1, 2, 3, 4, 5)
c = {1, 2, 3, 4, 5}
print(id(b))
print(id(c))
print(id(math))


#Functions and their Descriptions
#help()	 It is used it to find what other functions do
#hasattr()	Checks if an object has an attribute
#getattr()	Returns the contents of an attribute if there are some.
#repr()	 Return string representation of object
#callable() 	Checks if an object is a callable object (a function)or not.
#issubclass()	Checks if a specific class is a derived class of another class.
#isinstance()	Checks if an objects is an instance of a specific class.
#sys()	Give access to system specific variables and functions
#__doc__	Return some documentation about an object
#__name__	Return the name of the object.

# Technical Detail: The @functools.wraps decorator uses the function functools.update_wrapper()
# to update special attributes like __name__ and __doc__ that are used in the introspection.
import functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

""" A Few Real World Examples """
import functools
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator

# Timing functions
#creating a @timer decorator that measure the time a function takes to execute and print the duration to the console.


import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1 - storing the time just before the function starts running
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2 - storing the time after the function finishes
        run_time = end_time - start_time    # 3 - The time the function takes
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])
waste_some_time(99)
waste_some_time(1)


# A debugging decorator

# The following @debug decorator will print the arguments a function is called with
# as well as its return value every time the function is called:


import functools
def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        #Create a list of the positional arguments. Use repr() to get a nice string representing each argument.
        args_repr = [repr(a) for a in args]
        # Create a list of the keyword arguments. The f-string formats each argument as key=value where the !r specifier means that repr() is used to represent the value.
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        # the lists of positional and keyword arguments is joined together to one signature string with each argument separated by a comma.
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")   # The return value is printed after the function is executed
        return value
    return wrapper_debug
# how the decorator works in practice by applying it to a simple function with one position and one keyword argument:
@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"
#how the @debug decorator prints the signature and return value of the make_greeting() function:
make_greeting("Benjamin")
make_greeting("Richard", age=112)
make_greeting(name="Dorrisile", age=116)

# calculating an approximation to the mathematical constant e:

import math
import functools

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        #Create a list of the positional arguments. Use repr() to get a nice string representing each argument.
        args_repr = [repr(a) for a in args]
        # Create a list of the keyword arguments. The f-string formats each argument as key=value where the !r specifier means that repr() is used to represent the value.
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        # the lists of positional and keyword arguments is joined together to one signature string with each argument separated by a comma.
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")   # The return value is printed after the function is executed
        return value
    return wrapper_debug

# Apply a decorator to a standard library function
#math.factorial = debug(math.factorial)
@debug
def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))
approximate_e(5)
# The above example shows how you can apply a decorator to a function that has already been defined.
# The approximation of e is based on the series for calculating mathematical constant e

# Another example on slowing down code
# The @slow_down decorator will sleep one second before it calls the decorated function
# The most common use case is that you want to rate-limit a function that continuously checks whether a resource—like a web page—has changed.

import functools
import time

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)  # The countdown() function is a recursive function
countdown(3)


# Another example on registering plugins
# Decorators don’t have to wrap the function they’re decorating. They can also simply register that a function exists and return it unwrapped.
# This can be used, for instance, to create a light-weight plug-in architecture:

import random
PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)

print(randomly_greet("Alice"))
#The @register decorator simply stores a reference to the decorated function in the global PLUGINS dict.
# Note that you do not have to write an inner function or use @functools.wraps in this example because you are returning the original function unmodified.
# The randomly_greet() function randomly chooses one of the registered functions to use.
# Note that the PLUGINS dictionary already contains references to each function object that is registered as a plugin
# The main benefit of this simple plugin architecture is that you do not need to maintain a list of which plugins exist.
# That list is created when the plugins register themselves. This makes it trivial to add a new plugin: just define the function and decorate it with @register.
# Using the @register decorator, you can create your own curated list of interesting variables, effectively hand-picking some functions from globals().


# The following example is used when working with a web framework.
# In this example, we are using Flask to set up a /secret web page that should only be visible to users that are logged in or otherwise authenticated:
from flask import Flask, g, request, redirect, url_for
import functools
app = Flask(__name__)

def login_required(func):
    """Make sure user is logged in before proceeding"""
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required

@app.route("/secret")
@login_required
def secret():
    ...
# While this gives an idea about how to add authentication to your web framework, you should usually not write these types of decorators yourself.
# For Flask, you can use the Flask-Login extension instead, which adds more security and functionality.

""" Fancy Decorators """
# Decorating classes

#  The @classmethod and @staticmethod decorators are used to define methods inside a class namespace that are not connected to a particular instance of that class.
#  The @property decorator is used to customize getters and setters for class attributes.
# using the three decorators in a circle class
class Circle:
    def __init__(self,radius):
        self._radius = radius

    @property
    def radius(self):
        """ Get value of radius """
        return self._radius
    @radius.setter
    def radius(self,value):
        """ Set value of radius and return error if negative """
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self):
        """ Calculate area inside the circle """
        return self.pi() * self.radius ** 2

    def cylinder_volume(self,height):    # cylinder_volume() is a regular method.
        """ calculating the volume using circle as base"""
        return self.area * height

    @classmethod
    def unit_circle(cls):   # unit_circle() is a class method. It’s not bound to one particular instance of Circle.
        # Class methods are often used as factory methods that can create specific instances of the class.
        """Factory method creating a circle with radius 1"""
        return cls(1)

    @staticmethod
    def pi():  # pi() is a static method. It’s not really dependent on the Circle class, except that it is part of its namespace
        """Value of π, could use math.pi instead though"""
        return 3.1415926535
c = Circle(5)
print(c.radius)
print(c.area) # area is an immutable property: properties without .setter() methods can’t be changed.
# Even though it is defined as a method, it can be retrieved as an attribute without parentheses.
c.radius = 2 # radius is a mutable property: it can be set to a different value.
# We can do some error testing to make sure it’s not set to a nonsensical negative number. Properties are accessed as attributes without parentheses.
print(c.area)
print(c.cylinder_volume(height=4))
#c.area = 100
c = Circle.unit_circle()
print(c.radius)
print(c.pi())
print(Circle.pi())

""" defining a class where we decorate some of its methods using the @debug and @timer decorators from earlier"""
from decorator import debug, timer

class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer      # Here, @timer only measures the time it takes to instantiate the class
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])
tw = TimeWaster(1000)
tw.waste_time(999)

""" Another way to use decorators on classes is to decorate the whole class"""
from dataclasses import dataclass
@dataclass
class PlayingCard:
    rank: str
    suit: str
# Here you could have done the decoration by writing PlayingCard = dataclass(PlayingCard).


""" Nesting Decorators """
# applying several decorators to a function by stacking them on top of each other

#python program to demonstrate nested decorators
from decorator import debug, do_twice

@debug
@do_twice   # debug(do_twice(greet())) - debug calls do twice which calls greet
def greet(name):
    print(f"Hello {name}")

greet("Mark")

# interchanging the decorators

from decorator import debug, do_twice
@do_twice
@debug   # do_twice will be applied to debug as well
def greet(name):
    print(f"Hello {name}")

greet("Mark")


""" Decorators with arguments """
# passing arguments to your decorators

@repeat(num_twice=4)
def greet(name):
    print(f"Hello {name}")

# you then need repeat(num_times=4) to return a function object that can act as a decorator:
def repeat(num_times):
    def decorator_repeat(func):
      # create and return a wrapper function
      return decorator_repeat
# Typically, the decorator creates and returns an inner wrapper function, so writing the example out in full will give you an inner function within an inner function.
import functools

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat
@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")
greet("Tom Keen")
# We have put the same decorator pattern(wrapper) inside one additional def that handles the arguments to the decorator
# The wrapper_repeat() function takes arbitrary arguments and returns the value of the decorated function, func()
# This wrapper function also contains the loop that calls the decorated function num_times times.
# This wrapper function is not different except except that it is using the num_times parameter that must be supplied from the outside.
# The num_times argument is seemingly not used in repeat() itself.
# But by passing num_times a closure is created where the value of num_times is stored until it will be used later by wrapper_repeat().

""" Decorators that can be used both with and without arguments """
# when a decorator uses arguments you need to add an extra outer function for the code to figure out
# if the decorator has been called with or without arguments
# Decorators arguments must be specified by keywords
# You can enforce this with a special parameter *syntax which means the following parameters are keyword only
# func acts as a marker,noting whether the decorator has been called with arguments or not
# def name(_func=None, * ,kw1=val1, kw2=val2 ...):
#     def decorator_name(func):
#         # create and return a wrapper function
#     if _func is None:
#         return decorator_name    # the decorator was called with arguments
#     else:
#         return decorator_name(_func)  # the decorator was called without arguments
# If name has been called without arguments the decorated function will be passed in as _func
# If it has been called with arguments then _func will be none and some of
# the keyword arguments may have been changed from their default values
# The * in the argument list means the remaining arguments cant be called as positional arguments

import functools


def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)
@repeat
def surprise():
    print("Alaa!")


@repeat(num_times=4)  # default value of num is 2
def greet(name):
    print(f"Hi {name}")
surprise()
greet("Mark")


""" Stateful Decorators """
# decorators that can keep track of a state
# Example - decorator that counts the number of times a function is called
import functools


def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args,**kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args,**kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls


@count_calls
def say_whee():
    print("Whee!")


say_whee()
say_whee()


""" Classes as decorators """
# Example
# use of __call___ method


class MyDecorator:
    def __init__(self,count):
        self.decorator = count

    def __call__(self):
        self.decorator()


@MyDecorator
def greet():
    print("Mark")
greet()


# class decorator with args and kwargs
class MyDecorator:
    def __init__(self,count):
        self.math = count

    def __call__(self, *args, **kwargs):
        self.math(*args, **kwargs)
@MyDecorator
def greet(name,message):
    print("{} {}".format(message, name))
greet("Mark","Hi")


# class decorator with return statement
class SquareDecorator:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        # before function
        result = self.function(*args, **kwargs)

        # after function
        return result


# adding class decorator to the function
@SquareDecorator
def get_square(n):
    print("given number is:", n)
    return n * n

print("Square of number is:", get_square(195))


# Using class decorators to print time required to execute a program
from time import time
class Timer:
    def __init__(self,func):
        self.function = func

    def __call__(self, *args, **kwargs):
        start_time = time()
        result =self.function(*args, **kwargs)
        end_time = time()
        print("Execution took {:.4f} seconds".format(start_time-end_time))
        return result

# introducing some delay to simulate a time taking function
@Timer
def some_func(delay):
    from time import sleep
    sleep(delay)

some_func(2)

# checking error parameter using class decorator
# This decorator checks parameters before executing the function
# preventing the function to become overloaded and enables it to store only logical and necessary statements.
class ErrorCheck:

    def __init__(self, function):
        self.function = function

    def __call__(self, *params):
        if any([isinstance(i, str) for i in params]):
            raise TypeError("parameter cannot be a string !!")
        else:
            return self.function(*params)


@ErrorCheck
def add_numbers(*numbers):
    return sum(numbers)


#  returns 6
print(add_numbers(1, 2, 3))

# raises Error.
print(add_numbers(1, '2', 3))


# Example 2
class Counter:
    def __init__(self,start=0):
        self.count = start

    def __call__(self):
        self.count += 1
        print(f"Current count is {self.count}")
counter = Counter()
counter = Counter()
counter()
counter()
print(counter.count)


# Updated example
import functools

class CountCalls:

    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self,*args, **kwargs):
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        self.num_calls += 1
        return self.func(*args, **kwargs)

@CountCalls
def say_whee():
    print("Whee!")
say_whee()
say_whee()
print(say_whee.num_calls)


""" More Real World Examples """
# the previous @slow down calculator sleeps for one second
# introducing an optional rate argument that controls how long it sleeps
import functools
import time

def slow_down(_func= None, *,rate=1):
    """ Sleep given amount of seconds before calling the function """
    def decorator_slow_down(func):
        @functools.wraps(func)
        def wrapper_slow_down(*args,**kwargs):
            time.sleep(rate)
            return func(*args,**kwargs)
        return wrapper_slow_down

    if _func is None:
        return decorator_slow_down
    else:
        return decorator_slow_down(_func)

@slow_down(rate = 1)
def countdown(from_number):
    if from_number <1:
        print("Lit off!")
    else:
        print(from_number)
        countdown(from_number -2)

countdown(6)

""" Creating singletons """
# A singleton is a class with only one instance
# The following @singleton decorator turns a class into a singleton by storing the first instance of the class as an attribute
import functools
def singleton(cls):  # we are using cls instead of func as a parameter name to indicate that it is meant to be a class decorator
    """ Making a class a singleton class """
    @functools.wraps(cls)
    def wrapper_singleton(*args,**kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args,**kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton

@singleton
class TheOne:
    pass

first_one = TheOne()
another_one = TheOne()
print(id(first_one))
print(id(another_one))
print(first_one is another_one)

""" Caching return values """
# recursive definition of the fibonacci sequence

import functools

def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(10))
print(fibonacci.num_calls)

# To calculate the tenth Fibonacci number, you should really only need to calculate the preceding Fibonacci numbers
# but this implementation somehow needs a whopping 177 calculations.This is because the code keeps recalculating Fibonacci numbers that are already known.
#The usual solution is to implement Fibonacci numbers using a for loop and a lookup table.
# However, simple caching of the calculations will also do the trick:

import functools

def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

def cache(func):
    """Keep a cache of previous function calls"""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache

@cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

fibonacci(10)


# using @functools.lru_cache instead of writing your own cache decorator:
import functools

@functools.lru_cache(maxsize=4)
def fibonacci(num):
    print(f"Calculating fibonacci({num})")
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(10))
print(fibonacci.cache_info())
# The maxsize parameter specifies how many recent calls are cached

""" Adding Information about units """
# The following example does not really change the behaviour of the decorated function instead it adds a function to the decorated attribute
def set_unit(unit):
    """ set a unit on the func"""
    def decorator_set_unit(func):
        func.unit = unit
        return func
    return decorator_set_unit

import math
@set_unit("cm^3")
def volume(radius,height):
    return math.pi*radius**2*height

print(volume(2,3))
print(volume.unit)


# you could achieve similar using (functions annotations):
#However, since annotations are used for type hints, it would be hard to combine such units as annotations with static type checking.
# Units become even more powerful and fun when connected with a library that can convert between units. One such library is pint.
# With pint installed (pip install Pint), you can for instance convert the volume to cubic inches or gallons:


def set_unit(unit):
    """ set a unit on the func"""
    def decorator_set_unit(func):
        func.unit = unit
        return func
    return decorator_set_unit

import math
@set_unit("cm^3")
def volume(radius, height):
    return math.pi * radius**2 * height

import pint
ureg = pint.UnitRegistry()
vol = volume(3, 5) * ureg(volume.unit)

print(vol)
print(vol.to("cubic inches"))
print(vol.to("gallons").m) # Magnitude


#You could also modify the decorator to return a pint Quantity directly.
# Such a Quantity is made by multiplying a value with the unit.
# In pint, units must be looked up in a UnitRegistry.
# The registry is stored as a function attribute to avoid cluttering the namespace:
import functools
def use_unit(unit):
    """Have a function return a Quantity with given unit"""
    use_unit.ureg = pint.UnitRegistry()
    def decorator_use_unit(func):
        @functools.wraps(func)
        def wrapper_use_unit(*args, **kwargs):
            value = func(*args, **kwargs)
            return value * use_unit.ureg(unit)
        return wrapper_use_unit
    return decorator_use_unit

@use_unit("meters per second")
def average_speed(distance, duration):
    return distance / duration

bolt = average_speed(100, 9.58)
print(bolt)
print(bolt.to("km per hour"))
print(bolt.to("mph").m) # Magnitude


""" Validating json """
from flask import Flask, request, abort
import functools
app = Flask(__name__)

def validate_json(*expected_args):                  # 1
    def decorator_validate_json(func):
        @functools.wraps(func)
        def wrapper_validate_json(*args, **kwargs):
            json_object = request.get_json()
            for expected_arg in expected_args:      # 2
                if expected_arg not in json_object:
                    abort(400)
            return func(*args, **kwargs)
        return wrapper_validate_json
    return decorator_validate_json

@app.route("/grade", methods=["POST"])
@validate_json("student_id")
def update_grade():
    json_data = request.get_json()
    # Update database.
    return "success!"



""" Args and kwargs """
# passing a varying number of arguments using lists
def my_sum(my_list):
    result = 0
    for x in my_list:
        result += x
    return result


my_list = [2,4,6]
print(my_sum(my_list))  # implementation works but whenever you call this function you need to create a list of arguments to pass to it
# This can be inconvenient, especially if you don’t know up front all the values that should go into the list.


# example 2
def my_sum(my_integers):
    result = 7
    for x in my_integers:
        result += x
    return result


list_of_integers = [1, 2, 3]
print(my_sum(list_of_integers))


# Args allow to pass a varying number of positional arguments
def my_sum(*args):
    result=0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result
print(my_sum(2,4,6)) # no longer passing a list to my_sum;passing three  positional arguments and packing them all into a single iterable object named args.
# args is just a name,you can use *integers - * is the unpacking operator and its all that matters

""" kwargs """
# **kwargs works just like *args, but instead of accepting positional arguments it accepts keyword (or named) arguments.
def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
# Note that in the example above the iterable object is a standard dict. If you iterate over the dictionary and want to return its values then you must use .values().
        result += arg
    return result


print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

""" Ordering values in a function - standard arguments,args,kwargs """
def my_function(a, b, *args, **kwargs):
    pass


""" Unpacking With the Asterisk Operators: * - used on any iterable that Python provides & ** - only on dictionaries"""
my_list = [1, 2, 3]
print(my_list)  # printed along with corresponding brackets and commas

# unpacking
my_list = [1, 2, 3]
print(*my_list) # only prints the contents in the list


# using this method to call functions -  takes all the items of a list as though they were single arguments.
def my_sum(a,b,c):
    print(a+ b + c)


my_list = [1, 2, 3]
my_sum(*my_list)


#  using * operator to unpack a list and pass arguments to a function,it passes every single argument alone.
def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result


list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

print(my_sum(*list1, *list2, *list3))

# merging_lists
my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]

print(my_merged_list)

# extract_list_body
my_list = [1, 2, 3, 4, 5, 6]

a, *b, c = my_list

print(a)
print(b)
print(c)


""" Geeks for geeks """


# defining a decorator
def hello_decorator(func):
    # inner1 is a Wrapper function in
    # which the argument is called

    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behavior
function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
function_to_be_used()