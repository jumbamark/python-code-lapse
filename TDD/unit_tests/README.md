## Unit Testing
- __"Trust but verify with unit testing"__ ~ Shakespeare
- Change is one constant in programming. Languages evolve. Engineers may come and go, but if you use unittest then you will be more confident about upgrading andimproving existing code without causing problems for others
- Do not fear tests, embrace them
- __"The only thing we have to fear is a lot of failure messages when running our unit tests__  ~ Franklin Roosevelt
- unittest supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections and independence of the tests from the reporting framework.
- To achieve this unittest supports some important concepts in an object-oriented way:
	1. test fixture
	2. test case
	3. test suite
	4. test runner

## Command-Line Interface
- The unittest module can be used from the command line to run tests from modules, classes or even individual test methods:
	`python -m unittest test_module1 test_module2`
	`python -m unittest test_module.TestClass`
	`python -m unittest test_module.TestClass.test_method`

- Test modules can be specified by file path as well:
	`python -m unittest tests/test_something.py`

- You can run tests with higher verbosity by passing the `-v` flag
	`python -m unittest -v test_module`

- For a list of command-line options:
	`python -m unittest -h`

### Test Discovery
- The command line can also be used for test discovery, for running all of the tests in a project or just a subset

### Organizing test code
- Tests can be numerous and their set-up can be repetitive
- We can factor out set-up code by implementing a method called `setUp()` which the testing framework will automatically call for every single test we run
- Similarly we can provide a `tearDown()` method that tidies up after the test method has been run
- It is recommended that you use TestCase implementations to group tests together according to the features they test
- `unittest` provides a mechanism for this: the test suite represented by `unittest`'s `TestSuite` class

### Skipping tests and expected failures
- unittests supports skipping individual test methods and even whole classes of tests
- It also supports marking tests as an "expected failure", a test that is broken and will fail but shouldn't be counted as a failure on a __TestResult__
- Classes can also be skipped just like methods


## Classes and Functions
### Test cases
- 
