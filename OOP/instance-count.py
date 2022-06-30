"""Module that counts instance with class attributes
Uses public class attribute
"""


class C:
    """Represents a class C

    Attributes:
        counter (int): number of instances

    """

    counter = 0

    def __init__(self):
        """Method to initialize the C object.
        """
        type(self).counter += 1

    def __del__(self):
        """Method called after an instance is deleted
        """
        type(self).counter -= 1


if __name__ == "__main__":
    x = C()
    print("Number of instances::" + str(C.counter))
    y = C()
    print("Number of instances::" + str(C.counter))
    del x
    print("Number of instances::" + str(C.counter))
    del y
    print("Number of instances::" + str(C.counter))


