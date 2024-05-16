"""
This file contains a beautiful code that passes pycodestyle checks
"""

class Robot:
    """
    Creates a robot with a name and shows when it dies
    """
    population = 0

    def __init__(self, name):
        """
        initializing data
        """
        self.name = name
        print("(Initializing {})".faormat(self.name))

        population += 1

    def die(self):
        """
        I am dying
        """
        print("({} is being destroyed)".format(self.name))

        population -= 1

        if Robot.population == 0:
            print("{} was the last one".format(self.name))
        else:
            print("There are stills {:d} robots working".format(Robot.population))

    def say_hi(self):
        """
        Robot can greet
        """
        print("Hello, my creator calls me {}".format(self.name))

    @classmethod
    def how_many(cls):
        """
        prints the current population
        """
        print("We have {:d} robot".format(cls.population))