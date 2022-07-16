# the first argument to the testmod() is a module containing code to be scanned for tests

import doctest_simple

if __name__ == '__main__':
    import doctest
    doctest.testmod(doctest_simple, verbose=True)
