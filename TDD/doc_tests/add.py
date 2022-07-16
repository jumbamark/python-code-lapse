"""
Checking Examples in a Text File
"""

def simple_addition(a: int, b: int) -> int:
    assert type(a) == int and type(b) == int, "ints not used"
    return a + b

import doctest
doctest.testfile("add.txt")
