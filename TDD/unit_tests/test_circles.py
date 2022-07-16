import unittest
from circles import circle_area
from math import pi
"""
TestCircleArea:  subclass of the TestCase class in unittest module
run :
    python -m unittest test_circles
        -m instructs python to run the unittest as a script
    python -m unittest
        python will use the test discovery process where it will search for
        tests and run them.

Python has many methods (beyond assertAlmostEqual and AssertRaises)
One way to learn about a particular assert method is by lookiing at the
help text in interactive mode;
    suppose you want to learn more about assertSetEqual:
        ``import unittest``
        ``help(unittest.TestCase.assertSetEqual)``
"""


class TestCircleArea(unittest.TestCase):
    """
    each unittests starts with test
    """

    def test_area(self):
        """Test area when radius >= 0
        if correct to 7dp it assumes they are equal
        """
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi*2.1 ** 2)

    def test_values(self):
        """Make sure value erros are raised when necessary
        function should raise a Valueerror when input is a negative number
        To check that an exception is raised - assertRaises
        """
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        """Raise TypeError whenever the input is not a real number
        exceeption is raised when the input is a complex number,
        a boolean or string
        """
        self.assertRaises(TypeError, circle_area, 3 + 5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius")
