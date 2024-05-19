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

    prompt = "(hbnb) "

    classes = ['BaseModel']

    commands = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def precmd(self, arg):
        """
        Parses command input
        """
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cmd = cls[1].split('(')
            args = cmd[1].split(')')
            if cls[0] in HBNBCommand.classes and cmd[0] in HBNBCommand.commands:
                arg = cmd[0] + ' ' + cls[0] + ' ' + args[0]
        return arg

    def do_quit(self, arg):
        """
        Quits to exit the command interpreter
        """
        return True

    def do_EOF(self, arg):
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

    def do_create(self, arg):
        """
        Usage: create <class>
        This command creates an instance of a given class
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            dct = {'BaseModel': BaseModel}
            model = dct[arg]()
            print(model.id)
            model.save()

    def do_show(self, arg):
        """
        Usage: show <class> <id>
        Prints the string representation of an
        instance based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:


if __name__ == '__main__':
    HBNBCommand().cmdloop()
