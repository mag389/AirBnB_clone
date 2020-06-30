#!/usr/bin/python3
""" the airbnb console entry point """
import cmd
import inspect
from models.base_model import BaseModel
from models.user import User
import shlex
from models import storage


class HBNBCommand(cmd.Cmd):
    """ the bnb console class """

    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City",
               "Amenity", "Place", "Review"]

    def preloop(self):
        """sets up the objects to be searchable by uid for deletion and
        json serialization later
        """
        return

    def postloop(self):
        """closes out the program, saves to json storage etc
        """
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

        if l[0] == "BaseModel":
            obj = BaseModel()
            print(obj.id)
            storage.new(obj)
            storage.save()
        elif l[0] == "User":
            obj = User()
            print(obj.id)
            storage.new(obj)
            storage.save()
        else:
            print("** class doesn't exist **")

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
        key = l[0] + "." + l[1]
        if key in storage.all().keys():
            print(storage.all()[key])
            return
        else:
            print("** no instance found **")

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
        key = l[0] + "." + l[1]
        if key in storage.all().keys():
            storage.all().pop(key)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all object of certain type, or all objects
        """
        l = line.split()
        obj_list = []

        if len(l) < 1:
            for obj in storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
        else:
            classes = HBNBCommand.classes
            if l[0] not in classes:
                print("** class doesn't exist **")
                return
            for key in storage.all().keys():
                if key[0:len(l[0])] == l[0]:
                    obj_list.append(str(storage.all()[key]))
            print(obj_list)

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
        key = l[0] + "." + l[1]
        if key not in storage.all().keys():
            print("** no instance found **")
            return
        if len(l) < 3:
            print("** attribute name missing **")
            return
        if len(l) < 4:
            print("** value missing **")
            return

        setattr(storage.all()[key], l[2],
                type(getattr(storage.all()[key], l[2]))(l[3]))
        storage.all()[key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
