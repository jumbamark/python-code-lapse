"""
tracebacks are a special case of changing data
Since the paths in a traceback depend on the location where a module is installedon the
file system, it would be impossible to write portable tests if they were treated the
same as other output
doctests makes a special effort to recognize tracebacks and ignore the parts that
might change from system to system
"""
def this_raises():
    """This function always raises an exception.

    >>> this_raises()
    Traceback (most recent call last):
    RuntimeError: here is the error

    >>> this_raises()
    Traceback (innermost last):
    RuntimeError: here is the error
    """
    raise RuntimeError('here is the error')
