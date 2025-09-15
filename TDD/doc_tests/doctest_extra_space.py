"""
Whitespace within a line can aldo cause tricky problems with tests
This example has an extra space after 6
"""

def my_function(a,b):
    """
    >>> my_function(2, 3)
    6 
    >>> my_function('a',3)
    'aaa'
    """
    return a*b
