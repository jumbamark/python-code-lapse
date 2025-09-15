# class definition, name/type, parent of the class
# our coordinate is going to be an object in python


class Coordinate(object):
    """Defines a point in an x, y plane
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # methods are procedural attributes that allow us to interact with
    # our objects

    def distance(self, other):
        """Euclidian distance formula

        x1 minus x2 squared plus y1 minus y2 squared and square root
        of all that

        Args:
            self (obj): instance of the object you are going to perform
                        the operation on.
            other (): other coordinate object for which I want to find
                      the distance from my self.

        """
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def __str__(self):
        """Defines an output when print is called on an object of this type

        When print is called on the instance of type Coordinate:
        "c is an object of type Coordinate at a certain memory location"
        When print is called when there is the `__str__`:
        "call this method, look what it does and do everything inside it"

        Args:
            self (obj): calling print on the object itself

        Returns:
            str: `__str__` has to return a string.

        """
        return "<" + str(self.x) + "," + str(self.y) + ">"

# by default self is going to be the object C
c = Coordinate(3, 4)
origin = Coordinate(0, 0)

#calling print on an object of type Coordinate(calls the special method str)
# return of the __str__ method
print(c)

# the type of object c is a class Coordinate
print(type(c))

# a Coordinate is a class (class named Coordinate)
print(Coordinate)

# a Coordinate class is a type of object
print(type(Coordinate))

# using isinstance() to check if an object is a `Coordinate`
# True because c is an object that is of type Coordinate
print(isinstance(c, Coordinate))

print(c.x)
print(origin.x)

# object c is of type Coordinate, its(pyhton) going to look up at the class
# coordinate that you defined, its going to find the method called distance
# What parameters does it take? give it the other parameter
print(c.distance(origin))
print(Coordinate.distance(c, origin))


# Special Operators
# Just like `str` if you implement any of the special operators it 
# tells python when you use the plus operator between two objects of
# type coordinate to call this method:
"""
__add__(self, other) -> self + other
"""
