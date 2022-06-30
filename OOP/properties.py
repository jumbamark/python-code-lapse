# Properties vs. Getters and Setters
"""
Getters (accessors) and setters(mutators) are used in many object oriented programming languages to ensure the principle of data encapsulation
Data encapsulation is the bundling of data with the methods that operate on  them. These methods are the getter for retrieving and setter for changing
The python way to introduce attributes is to make them public

Properties
Properties offer a solution of having to add logic to our attributes without having to set getters and setters (our attributes remain public)
A method which is used for getting a value is decorated with "@property"
The method which has to function as the setter is decorated with "@x.setter"
If the function had been called "f" we would have to decorate it with "@f.setter"
"""

class P:
    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

if __name__ == "__main__":
    p1 = P(1001)
    print(p1.x)

# we could use different syntax without decorators to define the
# property but we'll have to use the getter function in the __init__ method

class P2:
    def __init__(self, x):
        self.set_x(x)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    x = property(get_x, set_x)

# This method goes against the Zen of Python because we now have 2 different
# ways to access or change the value of x, we can fix this by turning the
# getter and setter methods into private methods

class P3:
    def __init__(self, x):
        self.__set_x(x)

    def __get_x(self):
        return self.__x

    def __set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    x = property(__get_x, __set_x)


print("\n")


"""
class with internal attributes which can't be accessed from outside
shows that a property can be deduced from the values of more than one
attribute
"""
class Robot:
    def __init__(self, name, build_year, lk = 0.5, lp = 0.5):
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk
        self.__potential_psychic = lp

    @property
    def condition(self):
        s = self.__potential_physical + self.__potential_psychic
        if s <= -1:
            return "I feel miserable"
        elif s <= 0:
            return "I feel bad!"
        elif s <= 0.5:
            return "Could be worse!"
        elif s <= 1:
            return "Seems to be okay!"
        else:
            return "Great!"
if __name__ == "__main__":
    x = Robot("Marvin", 1979, 0.2, 0.4)
    y = Robot("Gerald", 1993, -0.4, 0.3)

    print(x.condition)
    print(y.condition)
