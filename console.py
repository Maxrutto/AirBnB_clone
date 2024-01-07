#!/usr/bin/env python
"""Defines the HBnB console"""
import cmd
from models import storage

class HBnBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter.
    Attributes:
        prompt (str): The prompt given to the user/developer
    """

    def emptyline(self):
        """Do nothing when receiving an empty line."""
        pass

    def do_quit(self):
        """Quit to exit the program."""
        return True

    def do_EOF(self):
        """EOF Signal to exit the program with a command"""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
