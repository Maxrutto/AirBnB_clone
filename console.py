#!/usr/bin/python3
"""Defines the HBnB console"""
import cmd

class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter.
    Attributes:
        prompt (str): The prompt given to the user/developer
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing when receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Quit to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF Signal to exit the program with a command"""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
