#!/usr/bin/python3
"""
BaseModel class that defines all common attributes/methods for other classes
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
        Summary: class that define the command interpreter:
    """
    # a custom prompt: (hbnb)
    prompt = "(hbnb) "

    doc_header = "Documented commands (type help <topic>):"
    ruler = '='

    # quit and EOF to exit the program
    def do_EOF(self, line):
        "Exit the program with Ctrl+D"
        return True

    def do_quit(slef, line):
        "Quit command to exit the program"
        return True

    # an empty line + ENTER shouldn’t execute anything
    def emptyline(self):
        """ If the line is empty, emptyline() is called,
            the method was modified because the default
            implementation runs the previous command again
            and we want it to pass not executing anything.
        """
        pass

if __name__ == "__main__":
    # Your code should not be executed when imported
    """ cmdloop() is the main processing loop of the interpreter. """
    HBNBCommand().cmdloop()
