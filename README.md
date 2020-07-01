# AirBnb clone

This is the repository for an airbnb clone project
The aim of which is to create a working Airbnb webapp.

This first section deals with the command interpreter/console.

The main way to use this console is interactively: you open it with the executable file
console.py from the terminal with ./console.py  \
Then when it gives the user a prompt you can give it commands.

### for example: 
>$ ./console.p\y
(hbnb) help\
\
documented commands (type help \<topic\>):\
========================================\
EOF  all  create  destroy  help  quit  show  update\
\
(hbnb)\
(hbnb) help quit\
Quit command to exit the program\
\
(hbnb)\
(hbnb)\
(hbnb) quit\

Alternatively you can use it in non-interactive mode by giving it commands frmo the terminal
> $ echo "help" | ./console.py\
(hbnb) \
Documented commands (type help \<topic\>):\
========================================\
EOF  all  create  destroy  help  quit  show  update\
$\

Once open this console is used for creating and maintaining airBNB objects\
i.e. python objects to represent them things such as users or places to rent.

to create a user open the console and give it the create command with the User option

> (hbnb) create User\
dc43729c-fe75-4e68-a851-5b51f9e0df55\
(hbnb) \

As you can see the console prints an ID number assoicated with that newly created User.
from there you can give that User new attributes such as a name, and display all\
 of that User's data with the update and show options respectively which each \
 take the User's ID in addition to other arguments
 >(hbnb) update User dc43729c-fe75-4e68-a851-5b51f9e0df55 first_name "john"\
 (hbnb) show User dc43729c-fe75-4e68-a851-5b51f9e0df55\
 [User] (dc43729c-fe75-4e68-a851-5b51f9e0df55) {'updated_at': datetime.datetime(2020, 7, 1, 19, 11, 52, 813453), 'id': 'dc43729c-fe75-4e68-a851-5b51f9e0df55', 'first_name': 'john', 'created_at': datetime.datetime(2020, 7, 1, 19, 5, 53, 652095)}
 \
 There are sevral other useful commands, for more info on specific commands use the help\
 option with the command as an argument.
