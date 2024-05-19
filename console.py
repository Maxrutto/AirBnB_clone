#!/usr/bin/python3
"""
This file contains the object representing the entry point
for the console

"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
    The entry point for the console
    Attributes:
        prompt (str): The prompt printed on the console
    """

    prompt = "(hbnb )"

    def do_quit(self):
        """
        Quits to exit the command interpreter
        """
        return True

    def do_EOF(self):
        """
        EOF signal to exit the program
        """
        print("")
        return True

    def emptyline(self):
        """
        When yo press enter it does nothing
        """
        pass

    def help_help(self):
        """
        Prints help description
        """
        print("Provides a description of a given command")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
