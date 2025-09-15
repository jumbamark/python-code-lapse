"""
The __init__ method
There are many method names which have special significance in Python classes.
The __init__ method is run as soon as an object of a class is instantiated.
The method is useful to do any initialization (passing initial values to your object) you want to do with your object.
"""

class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hello, my name is", self.name)

p = Person("Jumba Mark")
p.say_hi()

"""
We define the __init__ method as taking a parameter "name" (along with self)
We create a new field also called "name". The dotted notation self.name means that there is something called "name" that is part of the object called "self" and the other name is a local variable.

When creating new instance "p" of the class "Person" we do so by using the class name followed by the arguments in the paranthesis
Now we are able to use "self.name" field in our methods 
"""
