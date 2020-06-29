#!/usr/bin/python3
""" the airbnb console entry point """
import cmd
import inspect
from models.base_model import BaseModel
import shlex


class HBNBCommand(cmd.Cmd):
    """ the bnb console class """

    prompt = "(hbnb) "
    uids = {}
    classes = ["BaseModel", "User", "State", "City",
               "Amenity", "Place", "Review"]

    def preloop(self):
        """sets up the objects to be searchable by uid for deletion and
        json serialization later
        """
#        #serialize all objects form json
#        # add dictionary entry for each one with uid as key
        return

    def postloop(self):
        """closes out the program, saves to json storage etc
        """
#        #implement later
        print("ending console")
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
#        #if not a class print that
        try:
            var = eval(l[0] + "()")
            print(var.id)
            HBNBCommand.uids[var.id] = var
#            print(var)
# save to json file
        except NameError:
            print("**class doesn't exist **")

    def do_show(self, line):
        """prints string representation of object based on ID
        """
        classes = HBNBCommand.classes
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
        if l[1] in HBNBCommand.uids and \
                type(HBNBCommand.uids[l[1]]).__name__ == l[0]:
            print(HBNBCommand.uids[l[1]])
            return
        else:
            print("** no instance found **")
# check if instance id exists
# if so print object

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        classes = HBNBCommand.classes
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
        if l[1] in HBNBCommand.uids and \
                type(HBNBCommand.uids[l[1]]).__name__ == l[0]:
            HBNBCommand.uids.pop(l[1])
        else:
            print("** no instance found **")
#        check if instance id exist
#        destroy associated object

    def do_all(self, line):
        """Prints all object of certain type, or all objects
        """
        l = line.split()
# for now just all objects, incorrect form
        listy = []
        if len(l) < 1:
            for x in HBNBCommand.uids:
                listy.append(str(HBNBCommand.uids[x]))
            print(listy)
        else:
            classes = HBNBCommand.classes
            if l[0] not in classes:
                print("** class doesn't exist **")
                return
            for x in HBNBCommand.uids:
                if type(HBNBCommand.uids[x]).__name__ == l[0]:
                    listy.append(str(HBNBCommand.uids[x]))
#               #print(type(HBNBCommand.uids[x]).__name__)
#               #print(l[0])
            print(listy)

    def do_update(self, line):
        """updates an attribute of the object, us in form of
        update <class> <id> <attribute name> <new value>
        """
        l = shlex.split(line)
        if len(l) < 1:
            print("** class name missing **")
            return
        if l[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(l) < 2:
            print("** instance id missing **")
            return
        if l[1] not in HBNBCommand.uids or \
                type(HBNBCommand.uids[l[1]]).__name__ != l[0]:
            print("** no instance found **")
            return
        if len(l) < 3:
            print("** attribute name missing **")
            return
        if len(l) < 4:
            print("** value missing **")
            return
        setattr(HBNBCommand.uids[l[1]], l[2], l[3])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
