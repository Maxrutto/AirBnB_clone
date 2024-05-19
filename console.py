#!/usr/bin/python3
"""
This file contains the object representing the entry point
for the console

"""


import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import shlex


class HBNBCommand(cmd.Cmd):
    """
    The entry point for the console
    Attributes:
        prompt (str): The prompt printed on the console
    """

    prompt = "(hbnb) "

    classes = ['BaseModel']

    cmnds = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def precmd(self, arg):
        """
        Parses command input
        """
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cmd = cls[1].split('(')
            args = cmd[1].split(')')
            if cls[0] in HBNBCommand.classes and cmd[0] in HBNBCommand.cmnds:
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

        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            storage = FileStorage()
            all_objs = storage.all()
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Usage: destroy <class> <id>
        Deletes an instance based on the class name
        and id.
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            storage = FileStorage()
            all_objs = storage.all()
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    del value
                    del storage._FileStorage.__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """
        Usage: all <class>
        Prints all string representation of all instances
        """
        if arg not in HBNBCommand.classes:
            print("** class doesn't exist **")

        else:
            storage = FileStorage()
            all_objs = storage.all()
            list_instances = []
            for key, value in all_objs.items():
                obj_name = value.__class__.__name
                if obj_name == arg[0]:
                    list_instances += [value.__str__()]
            print(list_instances)

    def do_update(self, arg):
        """
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Updates an instance based on the class name and id by
        adding or updating attribute
        """
        if not arg:
            print("** class name missing **")
            return

        a = ""
        for argv in arg.split(','):
            a = a + argv

        args = shlex.split(a)

        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            storage = FileStorage()
            all_objs = storage.all()
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(value, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
