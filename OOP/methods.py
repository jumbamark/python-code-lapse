class Robot:
    pass

def hi(obj):
    print(f"Hi {obj.name}")

x = Robot()
x.name = "Mark"
hi(x)

# Binding the method hi to a class attribute
def hey(obj):
    print("Hey " + obj.name)

class Greetings:
    say_hi = hey

y = Greetings()
y.name = "Minayo Mary"
Greetings.say_hi(y)
# It is possible to define methods like this but there's a proper way to do it
y.say_hi()

# The __init__ method
"""
We want to define the attributes of an instance right after its creation
__init__ is a method which is immediately and automatically called after an instance has been created
"""

class Robots:
    def __init__(self, name=None):
        self.name = name

    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")


x = Robots()
x.say_hi()
y = Robots("Marvin")
y.say_hi()
