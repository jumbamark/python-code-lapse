""" Creating a module """


def fact(num):
    if num == 1:
        return num
    else:
        return num* fact(num -1)


def pal(x):
    x1 = x[::-1]
    if x1 == x:
        return "palindrome"
    else:
        return "not palindrome"


""""
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice
"""


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

