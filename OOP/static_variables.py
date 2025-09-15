# To create a static variable, we create it inside the class
#If you create a field outside of any other methods its automatically a static variable - its value is going to be shared by every object of type dog that is ever created

class Dog:
    num_of_dogs = 0

    # initialize our dog object
    def __init__(self, name="Unknown"):
        self.name = name

        # referencing the static variable(monitoring no of dogs)
        Dog.num_of_dogs += 1

    @staticmethod
    def getNumOfDogs():
            print("There are currently {} dogs".format(Dog.num_of_dogs))

def main():
    spot = Dog("Spot")
    doug = Dog("Doug")

    spot.getNumOfDogs()
    doug.getNumOfDogs()

main()
