"""
There are cases where it is beneficial to add extra whitespace in the sample output
for the test and have doctest ignore it
I.e data structures can be easier to read when spread across several lines even if 
their representation would fit on a single line


"""

def my_function(a, b):
    """Returns a*b

    >>> my_function(['A', 'B'], 3) #doctest: +NORMALIZE_WHITESPACE
    ['A', 'B',
     'A', 'B',
     'A', 'B']

    This does not match because of the extra space before ] and after the [ in the list
    >>> my_function(['A', 'B'], 2) #doctest: +NORMALIZE_WHITESPACE
    [ 'A', 'B',
      'A', 'B', ]
    """
    return a*b
