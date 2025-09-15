"""This module contains a Robot class utilizing static methods.
Uses private class attribute
"""


class Robot:
    """Represents a Robot class.

    Attributes:
        counter (int): stores the number of instances.
    """
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    @staticmethod
    def RobotInstances():
        return Robot.__counter

if __name__ == "__main__":
    print(Robot.RobotInstances())
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
    print(y.RobotInstances())
    print(Robot.RobotInstances())
