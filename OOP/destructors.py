"""
what holds true for constructors does so for destructors as well
__del__ is called when an instance is about to be destroyed and if there is no other reference to this instance
"""

class Robot():
    def __init__(self, name):
        print(name + "has been created")

    def __del__(self):
        print("Robot has been destroyed")


if __name__ == "__main__":
    x = Robot("Tik-Tok")
    y = Robot("Jenkins")
    z=x
    del x
    del y
