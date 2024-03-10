#!/usr/bin/python3
"""
This module defines a simple command-line interpreter for HBNB.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from shlex import split
import re


def parse_arguments(arg):
    """
    Parse arguments from the given string.

    Args:
        arg (str): The input string to be parsed.

    Returns:
        list: List of parsed arguments.
    """
    curly_braces_match = re.search(r"\{(.*?)\}", arg)
    brackets_match = re.search(r"\[(.*?)\]", arg)

    if curly_braces_match is None:
        if brackets_match is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets_match.span()[0]])
    else:
        lexer = split(arg[:curly_braces_match.span()[0]])

    arguments_list = [i.strip(",") for i in lexer]

    if curly_braces_match:
        arguments_list.append(curly_braces_match.group())
    elif brackets_match:
        arguments_list.append(brackets_match.group())

    return arguments_list


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class defines the command-line interpreter for HBNB.
    """
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """Exit the command-line interpreter."""
        return True

    def do_EOF(self, arg):
        """Exit the command-line interpreter on EOF."""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def default(self, arg):
        """Handle unknown commands."""
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            args = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", args[1])
            if match is not None:
                command = [args[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dict.keys():
                    call = "{} {}".format(args[0], command[1])
                    return arg_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_create(self, arg):
        """Create a new instance, save it, and print the new instance id."""
        args = parse_arguments(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = globals()[args[0]]()
            print(new_instance.id)
            storage.save()

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = parse_arguments(arg)
        obj_dict = storage.all()

        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = parse_arguments(arg)
        obj_dict = storage.all()

        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """Print all string representations of instances."""
        args = parse_arguments(arg)

        if args and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objs = [str(obj) for obj in storage.all().values() if not args or args[0] == obj.__class__.__name__]
            print('\n'.join(objs))

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        args = parse_arguments(arg)
        obj_dict = storage.all()

        if not args:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) < 2:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
            return False
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        if len(args) < 4:
            print("** value missing **")
            return False

        if args[2] in ["id", "created_at", "updated_at"]:
            print("** cannot update id, created_at, or updated_at **")
            return False

        obj = obj_dict["{}.{}".format(args[0], args[1])]
        attr_name = args[2]
        attr_value = args[3]

        # Update the attribute if it exists in the class
        if hasattr(obj, attr_name):
            # Get the type of the attribute and cast the value
            attr_type = type(getattr(obj, attr_name))
            setattr(obj, attr_name, attr_type(attr_value))
            storage.save()
        else:
            print("** attribute doesn't exist **")

    def do_count(self, arg):
        """Count and print the number of instances of a specified class."""
        args = parse_arguments(arg)

        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            count = sum(1 for obj in storage.all().values() if args[0] == obj.__class__.__name__)
            print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
