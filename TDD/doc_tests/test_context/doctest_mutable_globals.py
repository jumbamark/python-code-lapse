"""
The tests can still interfere with each other if they change the contents of mutable variables defined in the module
The module variable _module_data is changed by tests for one() causing the test for two() to fail
If global values are needed for the tests, to parameterize them for an environment for exaple,values can be passed to "testmod()" and "testfile()" to have the context set up using data controlled by the caller
"""

_module_data = {}

class TestGlobals:
    def one(self):
        """
        >>> TestGlobals().one()
        >>> 'var' in _module_data
        True
        """
        _module_data['var'] = 'value'

    def two(self):
        """
        >>> 'var' in _module_data
        False
        """
