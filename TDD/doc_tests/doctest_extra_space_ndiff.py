"""
Using one of the diff-based reporting options, such as REPORT_NDIFF, shows the
difference between the actual and expected values with more detail and the extra
space becomes visible
"""

def my_function(a, b):
    """
    >>> my_function(2, 3) # doctest: +REPORT_NDIFF
    6 

    >>> my_function('a', 3)
    'aaa'
    """
    return a*b
