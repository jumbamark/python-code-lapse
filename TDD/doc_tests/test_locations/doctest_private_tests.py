"""
There are cases where tests exist in a module that should be included with the source code but not in the help text for a module, so they need to be placed somewhere other than the docstrings.
doctests also looks for a module-level variable called "__test__" and uses it to locate other tests
The value of "__test__" should be a dictionary that maps test set names (as strings) to strings, modules, classes or functions

If the value associated with a key is a string, it is treated as a docstring and scanned for tests
If the value is a class or function, doctest searches them recursively for docstrings which are then scanned for tests (in the example below the imported module has a single test - after scanning there will be a total of five tests)
"""

import doctest_private_tests_external

__test__ = {
    'numbers': """
>>> my_function(2, 3)
6

>>> my_function(2.0, 3)
6.0
""",

    'strings': """
>>> my_function('a',3)
'aaa'

>>> my_function(3, 'a')
'aaa'
""",

    'external': doctest_private_tests_external,
}

def my_function(a, b):
    """Returns a*b
    """
    return a*b
