# below command will show the modules included
# and if it has double under score don't try to change it

# print(dir())

###################################################################
# below is the way to find out the functions included in builtins #
###################################################################

# print(dir(__builtins__))

# for m in dir(__builtins__):
#     print(m)

###################################################################
# below is the way to find out the functions included in builtins #
###################################################################
import shelve
import random

# print(dir())
# print()
# print(dir(shelve))


# below is the way to find the classes in shelve for example:- close

# for obj in dir(shelve.Shelf):
#     if obj[0] != '_':
#         print(obj)

help(shelve)    # this function will print the helpful info regarding shelve

# help(random.randint)

