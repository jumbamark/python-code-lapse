"""
There are cases where the exact output may not be predictable, but should be testable
Examples:
    local date and time values and object ids change on evry test run
    the default precision used in the representation of floating point values depend on
    compiler options
    string representation of container objects like dictionaries may not be deterministic
A way to get around it is use the ELLIPSIS option to tell doctest to ignore portions of the verification value
"""
# python3 -m doctest -v doctest_ellipsis.py


class MyClass:
    pass

def unpredictable(obj):
    """Returns a new list containing obj

    >>> unpredictable(MyClass()) # doctest: +ELLIPSIS
    [<doctest_ellipsis.MyClass object at 0x...>]
    """
    return [obj]
