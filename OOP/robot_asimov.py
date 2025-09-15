"""Module containing the "Three Laws of Robotics"
Isaac Asimov devised and introduced the so called "Three Laws of Robotics"
"""


class Robot:
    """Represents a Robot with name and build year

    Attributes:
        Three_Laws (tuple) : Robotic Laws

    """
    Three_Laws = (
            """A robot may not injure a human being or, through inaction, allow a human being to come to harm.""",
            """A robot must obey the orders given to it by human beings, except where such orders would conflict with the First Law.,""",
            """A robot must protect its own existence as long as such protection with the First or Second Law."""
            )

    def __init__(self, name, build_year):
        """Method to initialize the Robot object"""
        self.name = name
        self.build_year = build_year


# accessing the class attribute via instance or via class name
if __name__ == "__main__":
    for number, text in enumerate(Robot.Three_Laws):
        print(str(number + 1) + ":\n" + text)
