# Public, - Protected-, and Private Attributes
"""
name: public attributes can be freely used inside or outside a class definition
_name: protected attributes should not be used outside the class definition unless inside a subclass definition.
__name: private attributes are inaccessible and invisible. It's neither possible to read nor write to those attributes except inside the class definition itself
"""

class A():
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"

# Data Encapsulation means we should only be able to access private 
# attributes via getters and setters

class Robot:
    def __init__(self, name=None, build_year=2000):
        self.__name = name
        self.__build_year = build_year

    def say_hi(self):
        if self.__name:
            print("Hi, I am " + self.__name)
        else:
            print("Hi, I am a robot without a name")

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_build_year(self, by):
        self.__build_year = by

    def get_build_year(self):
        return self.__build_year

    def __repr__(self):
        return "Robot('" + self.__name + "', " + str(self.__build_year) +")"

    def __str__(self):
        return "Name:" + self.__name + ",Build Year:"+str(self.__build_year)

if __name__ == "__main__":
    x = Robot("Monty", 1979)
    y = Robot("Caribean", 1943)

for rob in [x, y]:
    rob.say_hi()
    if rob.get_name() == "Caribean":
        rob.set_build_year(1993)

    print("I was built in the year " + str(rob.get_build_year()) + " !")
