import functools


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


""" Module - 1 """

import functools


def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        # Create a list of the positional arguments.
        # Use repr() to get a nice string representing each argument.
        args_repr = [repr(a) for a in args]
        # Create a list of the keyword arguments. The f-string formats each argument
        # as key=value where the !r specifier means that repr() is used to represent the value.
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        # the lists of positional and keyword arguments is joined
        # together to one signature string with each argument separated by a comma.
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")   # The return value is printed after the function is executed
        return value
    return wrapper_debug


""" module - 2 """


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
