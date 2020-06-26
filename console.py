#!/usr/bin/python3
""" the airbnb console entry point """
import cmd
import inspect
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ the bnb console class """

    prompt = "(hbnb) "
    uids = {}

    def preloop(self):
        """sets up the objects to be searchable by uid for deletion and 
        json serialization later
        """
        #serialize all objects form json
        # add dictionary entry for each one with uid as key
        return

    def postloop(self):
        """closes out the program, saves to json storage etc
        """
        #implement later
        pass

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
            HBNBCommand.uids[var.id] = var
            print(var)
# save to json file
        except NameError:
            print("**class doesn't exist **")

    def do_show(self, line):
        """prints string representation of object based on ID
        """
        classes = ['BaseModel', 'User']
        l = line.split()
        if len(l) < 1:
            print("** class name missing **")
            return
        if l[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(l) < 2:
            print("** instance id missing **")
            return
#check if instance id exists
#if so print object

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        classes = ['BaseModel', 'User']
        l = line.split()
        if len(l) < 1:
            print("** class name missing **")
            return
        if l[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(l) < 2:
            print("** instance id missing **")
#        check if instance id exist
#        destroy associated object

    def do_all(self, line):
        """Prints all object of certain type, or all objects
        """
#for now just all objects, incorrect form
        print(list(HBNBCommand.uids))


if __name__ == '__main__':
    HBNBCommand().cmdloop()