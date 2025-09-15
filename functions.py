def f():
    s = "__ Inside f()"
    print(s)


print("Before calling f()")
f()
print("After calling f()")

# empty function
# usually a temporary place holder for a python function that will be fully implemented at a later time.


def f():
    pass


f()   # it is syntactically valid but doesn't do anything


# Argument passing
# positional arguments/required arguments - must be specified in the exact order, same number of arguments


def f(qty, item, price):   # parameters
    print(f"{qty} {item} cost Ksh.{price}")


f(6, "bananas", 30)  # arguments

# keyword arguments
# referencing a key word that does not match any of the declared parameters generates an exception
# they lift the restriction on argument order


def f(qty, item, price):  # parameters
    print(f"{qty} {item} cost Ksh.{price}")


f(item="bananas", price=30, qty=6)
# a function can be called using both positional and key word arguments, positional arguments come first

# Default parameters
# when ths version of f is called any argument that is left out assumes it's default value


def f(qty=6, item="bananas", price=30.769):
    print(f"{qty} {item} cost Ksh.{price:.2f}")


f()
f(4)
f(4, "apples")
f(4, "apples", 30.568)
f(price=2.29)
f(item="Mats", qty=3)

# Multiple default parameter values
# the default parameter for my list is an empty list,so if f is called without arguments,the return value will be ###


def f(my_list=[]):
    my_list.append("###")
    return my_list


print(f([1, 2, 3, 4, 5]))
f()
f()  # each time you  call f you are performing append on the same list bec default parameters are defined only once

# to avoid this use a default argument that signals no argument has been specified


def f(my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(["###"])
    return my_list


print(f())
print(f())


# return statement
def double_list(x):
    i = 0
    while i < len(x):
        x[i] *= 2
        i += 1


a = [1, 2, 3, 4, 5]
double_list(a)
print(a)

# using return statement


def double_list(x):
    r = []
    for i in x:
        r.append(i * 2)
    return r


a = [1, 2, 3, 4, 5]
a = double_list(a)
print(a)

# variable-length argument lists


def avg(a):
    total = 0
    for i in a:
        total += i
    return total/len(a)


print(avg([1, 2, 3, 4, 5]))


# argument tuple parking
# parameter names preceded by asterisk indicate argument tuple parking


def f(*args):
    print(args)
    print(type(args), len(args))
    for i in args:
        print(i)


f(1, 2, 3, 4)

# argument dictionary unpacking
# parameter name preceded by double asterisk indicate corresponding values which are expected to be key value pairs
# should be packed into a dictionary


def f(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, val in kwargs.items():
        print(key, "->", val)


f(foo=1, bar=2, bax=3)


# putting it all together
# order - positional parameters, args, kwargs


def f(a, b, *args, **kwargs):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")


f(1, 2, "foo", "bar", "baz","qux", x=100, y=200, z=300)


# multiple unpacking in a python function call


def f(*args):
    for i in args:
        print(i)

a = [1, 2, 3]
t = [4, 5, 6]
s = {7, 8, 9}

f(*a, *t, *s)


def f(**kwargs):
     for k, v in kwargs.items():
         print(k, "->", v)


d1 = {"a": 1, "b": 2}
d2 = {"x": 3, "y": 4}

f(**d1, **d2)


# Docstrings
# supplies documentation to a function


def avg(*args):
    """ Returns the average of a list of numeric values"""
    return sum(args/ len(args))


print(avg.__doc__)



