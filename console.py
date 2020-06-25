#!/usr/bin/python3
""" the airbnb console entry point """
import cmd


class HBNBCommand(cmd.Cmd):
    """ the bnb console class """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """quits the program may need to save things later
        """
        return True

    def do_EOF(self, line):
        """quits the program
        """
        return True

    def emptyline(self):
        """deals with empty line """
        pass

    def do_create(self, line):
        """Creaes new instance of basemodel
        """
        l = line.split()
        if len(l) < 1:
            print("** class name missing **")
            return
        #if not a class print that
        try:
            var = eval(l[0]+ "()")
            print(var.id)
        except NameError:
            print("**class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
