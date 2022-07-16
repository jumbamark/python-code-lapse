## Running Tests
- The previous examples use the command line test runner built into doctest
- It is easy and convenient for a single module but will quickly become tedious as a package spreads out into multiple files

### By Module
1. doctest_testmod.py
2. doctest_testmod_other_module.py

### By File
- `testfile()` works in a way similar to `testmod()` allowing the tests to be invoked explicitly in an external file from within the test program
    
    ```python
    # doctest_testfile.py
    import doctest

    if __name__ == '__main__':
        doctest.testfile('doctest_in_help.txt')
    ```

## Unittest Suite
- When both `unittest` and doctest are used for testing the same code in different situations, the unittest integration in doctest can be used to run the tests together
- Two classes, DocTestSuite and DocFileSuite create test suites compatible with the test-runner API of `unittest`

    ```python
    # doctest_unittest.py

    import doctest
    import unittest

    import doctest_simple

    suite = unittest.TestSuite()
    suite.addTest(doctest.DocTestSuite(doctest_simple))
    suite.addTest(doctest.DocFileSuite('doctest_in_help.txt'))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    ```
