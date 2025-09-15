class Animal:
    def __init__(self, birthType="Unknown", appearence="Unknown",
                 blooded="Unknown"):
        self.birthType = birthType
        self.appearence = appearence
        self.blooded = blooded

    @property
    def birthType(self):
        return self.__birthType

    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType


    @property
    def appearence(self):
        return self.__appearence

    @appearence.setter
    def appearence(self, appearence):
        self.__appearence = appearence


    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    def __str__(self):
        return "A {} is {} it is {} it has {}".format(type(self).__name__, self.birthType, self.appearence, self.blooded)


#inherit every getter and setter in general that's inside of the Animal class
class Mammal(Animal):
    def __init__(self, birthType="born alive",
                 appearence="hair or fur",
                 blooded="warm blooded",
                 nurseYoung=True):

        # call the initialization method inside of Animal from inside of our new Mammal
        # pass in all the things that the Animal initialization method can handle
        Animal.__init__(self, birthType, appearence, blooded)
        self.__nurseYoung = nurseYoung

    @property
    def nurseYoung(self):
        return self.__nurseYoung

    @nurseYoung.setter
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung = nurseYoung

    # overriding our magic string method
    # Another way to call for a method to run in another class is calling the super class
    def __str__(self):
        return super().__str__() + " and it has {} they nurse"\
                " their young".format(self.nurseYoung)


# Reptile class
class Reptile(Animal):
    def __init__(self, birthType="born in an egg or born alive", appearence="dry scales", blooded="cold blooded"):
        Animal.__init__(self, birthType, appearence, blooded)

    # function overloading (receiving an unknown number of variables
    def sumAll(self, *args):
        sum = 0

        for i in args:
            sum += 1
        return sum


# polymorphism
def getBirthType(theObject):
    print("the {} is {}".format(type(theObject).__name__, theObject.birthType))



if __name__ == '__main__':
    animal1 = Animal("born alive")
    print(animal1.birthType)
    print("-------")
    print(animal1)

    print()
    mammal1 = Mammal()
    print(mammal1)
    print(mammal1.birthType)
    print(mammal1.blooded)

    print()
    reptile1 = Reptile()
    print(reptile1)
    print(reptile1.birthType)

    print("Sum : {}".format(reptile1.sumAll(1, 2, 3, 4, 5)))
    print()
    getBirthType(mammal1)
    getBirthType(reptile1)
