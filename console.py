#!/usr/bin/python3
""" the airbnb console entry point """
import cmd
import inspect
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
import shlex
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """ the bnb console class """

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

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

        if l[0] in HBNBCommand.classes:
            obj = HBNBCommand.classes[l[0]]()
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

        if l[2] in storage.all()[key].to_dict().keys():
            setattr(storage.all()[key], l[2],
                    type(getattr(storage.all()[key], l[2]))(l[3]))
        else:
            setattr(storage.all()[key], l[2], l[3])
        storage.all()[key].save()

    def default(self, line):
        """the all printer"""
        l = line.split(".")
        if len(l) != 2:
            super().default(line)
            return
        if l[0] not in HBNBCommand.classes:
            super().default(line)
            return
        if l[1] == "all()":
            ret = []
            printed = 0
            print("[", end="")
            for key in storage.all().keys():
                # if key[0:len(l[0])] == l[0]:
                if isinstance(storage.all()[key], HBNBCommand.classes[l[0]]):
                    if printed == 1:
                        print(", ", end="")
                    ret.append(str(storage.all()[key]))
                    print(storage.all()[key], end="")
                    printed = 1
            print("]")
            return
        if l[1] == "count()":
            ret = 0
            for key in storage.all().keys():
                # if key[0:len(l[0])] == l[0]:
                if isinstance(storage.all()[key], HBNBCommand.classes[l[0]]):
                    ret += 1
            print(ret)
            return
        if l[1][0:4] == "show":
            if len(l[1][4:]) < 3:
                print("** instance id missing **")
                return
            id = l[1][5:-1]
            key = l[0] + "." + id
            if key in storage.all().keys():
                print(storage.all()[key])
                return
            else:
                print("** no instance found **")
                return
        if l[1][0:7] == "destroy":
            if len(l[1][7:]) < 3:
                print("** instance id missing **")
                return
            id = l[1][8:-1]
            key = l[0] + "." + id
            if key in storage.all().keys():
                storage.all().pop(key)
                return
            else:
                print("** no instance found **")
                return
        if l[1][0:6] == "update":
            if '{' in l[1]:
                args = HBNBCommand.split_with_dict(l[1][7:-1])

                if len(args) < 1:
                    print("** instance id missing **")
                    return
                key = l[0] + "." + args[0]
                if key not in storage.all().keys():
                    print("** no instance found **")
                    return
                if len(args) < 2:
                    print("** attribute name missing **")
                    return
                dict_string = ""
                for char in args[1]:
                    if char == "'":
                        dict_string += '"'
                    else:
                        dict_string += char
                attr_dict = json.loads(dict_string)
                print(attr_dict)
                for attr_key, value in attr_dict.items():
                    if attr_key in storage.all()[key].to_dict().keys():
                        setattr(storage.all()[key], attr_key,
                                type(getattr(storage.all()[key],
                                     attr_key))(value))
                    else:
                        setattr(storage.all()[key], attr_key, str(value))
                    storage.all()[key].save()
                return
            else:
                args = l[1][7:-1].split(", ")
                for index in range(0, len(args)):
                    if args[index][0] == '"' and args[index][-1] == '"':
                        args[index] = args[index][1:-1]

                if len(args[0]) == 0:
                    print("** instance id missing **")
                    return
                key = l[0] + "." + args[0]
                if key not in storage.all().keys():
                    print("** no instance found **")
                    return
                if len(args) < 2:
                    print("** attribute name missing **")
                    return
                if len(args) < 3:
                    print("** value missing **")
                    return
                if args[1] in storage.all()[key].to_dict().keys():
                    setattr(storage.all()[key], args[1],
                            type(getattr(storage.all()[key],
                                 args[1]))(args[2]))
                else:
                    setattr(storage.all()[key], args[1], args[2])
                storage.all()[key].save()
                return

        super().default(line)

    def split_with_dict(line):
        """ Breaks a line into arguments using ', ' as a separator
            while keeping a dictionary in one piece
        """
        args = []
        index = 0
        while index < len(line):
            token = ""
            if line[index] == '"':
                while index < len(line):
                    token += line[index]
                    index += 1
                    if line[index] == '"':
                        token += line[index]
                        index += 1
                        args.append(token)
                        break
            elif line[index] == '{':
                while index < len(line):
                    token += line[index]
                    index += 1
                    if line[index] == '}':
                        token += line[index]
                        index += 1
                        args.append(token)
                        break
            elif line[index] == ' ' or line[index] == ',':
                index += 1
            else:
                while index < len(line):
                    token += line[index]
                    index += 1
                    if line[index] == ' ' or line[index] == ',':
                        index += 1
                        args.append(token)
                        break

        for index in range(0, len(args)):
                    if args[index][0] == '"' and args[index][-1] == '"':
                        args[index] = args[index][1:-1]
        return args

if __name__ == '__main__':
    HBNBCommand().cmdloop()
