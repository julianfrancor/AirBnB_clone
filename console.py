#!/usr/bin/python3
"""
BaseModel class that defines all common attributes/methods for other classes
"""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
        Summary: class that define the command interpreter:
    """
    prompt = "(hbnb) "
    list_classes = ["BaseModel", "User", "Place", "State", "City",
                    "Amenity", "Review"]

    doc_header = "Documented commands (type help <topic>):"
    ruler = '='

    def do_EOF(self, line):
        "Exit the program with Ctrl+D"
        return True

    def do_quit(slef, line):
        "Quit command to exit the program"
        return True

    def emptyline(self):
        """ an empty line + ENTER shouldn’t execute anything
            If the line is empty, emptyline() is called,
            the method was modified because the default
            implementation runs the previous command again
            and we want it to pass not executing anything.
        """
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        """
        args_list = arg.split(" ")
        if not args_list[0]:
            print("** class name missing **")
        elif args_list[0] in HBNBCommand.list_classes:
            new_instance = globals()[args_list[0]]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of an instance
            based on the class name and id
        """
        args_list = arg.split(" ")
        if args_list[0] == "":
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.list_classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            """ We need to check if the 'id' exists, to do so we need to
            create id_object with the form Classname.id that is the key that
            we will ask if is in Storge and retrieve the value for that key
            """
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in storage.all():
                print("** no instance found **")
            else:
                """print the string representation based on the
                   class name and the ID
                """
                print(storage.all()[id_object])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id
            (save the change into the JSON file).
        """
        args_list = arg.split(" ")
        if args_list[0] == "":
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.list_classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            """ We need to check if the 'id' exists, to do so we need to
            create id_object with the form Classname.id that is the key that
            we will ask if is in Storge and retrieve the value for that key
            """
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in storage.all():
                print("** no instance found **")
            else:
                """deletes an instance for the dictionary
                """
                storage.all().pop(id_object)
                storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances based or not
            on the class name
        """
        element_list = []
        args_list = arg.split()
        if len(args_list) == 0:
            for key, value in storage.all().items():
                element_list.append(str(value))
            print(element_list)
        elif args_list[0] in HBNBCommand.list_classes:
            for key, value in storage.all().items():
                if value.__class__.__name__ == args_list[0]:
                    element_list.append(str(value))
            print(element_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
           updating attribute  (save the change into the JSON file).
        """
        args_list = shlex.split(arg)
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.list_classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        elif len(args_list) < 3:
            print("** attribute name missing **")
        elif len(args_list) < 4:
            print("** value missing **")
        else:
            "if the instance of the class name doesn’t exist for the id"
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in storage.all():
                print("** no instance found **")
            else:
                id_object = "{}.{}".format(args_list[0], args_list[1])
                name_attr = args_list[2]
                value = args_list[3]
                """ Only “simple” arguments can be updated: string,
                    integer and float. """
                if value.replace('.', '', 1).isdigit():
                    if args_list[3].isdigit():
                        value = int(value)
                    else:
                        value = float(value)
                setattr(storage.all()[id_object], name_attr, value)
                storage.all()[id_object].save()

    def do_count(self, arg):
        """Count the number of instances of a class"""
        count = 0
        for key, value in storage.all().items():
            if key.split(".")[0] == arg:
                count += 1
        print(count)

    def default(self, arg):
        """Method called on an input line when the command prefix is
        not recognized. If this method is not overridden, it prints an
        error message and returns. """
        # BaseModel show("440f0fd5-502f-4f46-bc09-6b2c1b156fa7")
        args_list = arg.split(".")
        if args_list[0] in HBNBCommand.list_classes:  # BaseModel
            method = args_list[1].split("(")  # show
            # retrieve all instances of a class by using: <class name>.all()
            if method[0] == "all":
                return self.do_all(args_list[0])
            # retrieve the number of instances of a class: <class name>.count()
            elif method[0] == "count":
                return self.do_count(args_list[0])
            elif method[0] == "show":
                # show( 440f0fd5-502f-4f46-bc09-6b2c1b156fa7 )
                id_show = args_list[1].split('"')
                args_show = "{} {}".format(args_list[0], id_show[1])
                return self.do_show(args_show)
            elif method[0] == "destroy":
                id_destroy = args_list[1].split('"')
                args_destroy = "{} {}".format(args_list[0], id_destroy[1])
                return self.do_destroy(args_destroy)
            elif method[0] == "update":
                # update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"
                # User.update("2f18e70a-bb66-4965-b3b4-b519e428b0c9", "first_name", "John")
                # User.update("2f18e70a-bb66-4965-b3b4-b519e428b0c9", "age", 35)
                part1 = method[1].split(")")  # "2f18e70a-bb66-4965-b3b4-b519e428b0c9", "first_name", "John")
                part2 = part1[0]. split(",")
                part3 = shlex.split(part2)
                args_update = "{} {} {} {}".format(args_list[0], part3[0], part3[1], part3[2])
                print(args_update)
                # return self.do_update(args_update)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
