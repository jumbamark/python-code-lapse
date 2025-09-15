"""This module contains a fraction class, which is incomplete

If you work with fractions, you need to be capable of simplifying them.
We can reduce a fraction to the lowest terms by dividing both the numerator
and denominator by GCD

"""

class fraction(object):
    """Represents a fraction with numerator and denominator"""

    def __init__(self, n, d):
        self.numerator, self.denominator = fraction.reduce(n, d)

    @staticmethod
    def gcd(a, b):
        """Calculates the GCD of the two numbers.
        """
        while b != 0:
            a, b = b, a%b
        return a

    @classmethod
    def reduce(cls, n1, n2):
        """
        The staic method is called by this classmethod "reduce"
        with "cls.gcd(n1, n2)". "CLS" is a reference to "fraction"
        """

        g = cls.gcd(n1, n2)
        return (n1 // g, n2 //g)

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

if __name__ == '__main__':
    x = fraction(8, 24)
    print(x)
