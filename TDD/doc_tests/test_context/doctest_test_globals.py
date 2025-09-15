"""
The execution context created by doctest as it runs tests contains a copy of the module-level globals for the test module
Each test source (function, class, module) has its own set of global values to isolate the tests from each other somewhat, so they are likely to interfere with one another
The tests in the docstring for one() set a global variable and the test for two() looks for it (expecting not to find it)
"""

class TestGlobals:
    def one(self):
        """
        >>> var = 'value'
        >>> 'var' in globals()
        True
        """

    def two(self):
        """
        >>> 'var' in globals()
        False
        """
