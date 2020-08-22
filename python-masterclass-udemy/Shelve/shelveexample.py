# don't use shelve file from untrusted source
# if you are using an import always make sure your import and file name are separate
# shelve is read and write by default so no need to mention the file opening mode
# by default shelve might create a DB file, in my case it created 3 files

import shelve

# # below is a shelve and not a dictionary
# with shelve.open('ShelfTest') as fruit:
#     fruit['orange'] = "a sweet, orange, citrus fruit"
#     fruit['apple'] = "good for making cider"
#     fruit['lemon'] = "a yellow, citrus fruit"
#     fruit['grape'] = "a small, sweet fruit growing in bunches"
#     fruit['lime'] = "a sour, green citrus fruit"
#
#     print(fruit["lemon"])
#     print(fruit["grape"])
#
# # below lines will give an error as we are trying to perform an invalid operation
# # on a closed shelf
# # print(fruit["lemon"])
# # print(fruit["grape"])
#
# print(fruit)     # this is printing out a closed shelf

###################################################
# below is an example of closing a shelf manually #
###################################################

fruit = shelve.open('ShelfTest')
# fruit['orange'] = "a sweet, orange, citrus fruit"
# fruit['apple'] = "good for making cider"
# fruit['lemon'] = "a yellow, citrus fruit"
# fruit['grape'] = "a small, sweet fruit growing in bunches"
# fruit['lime'] = "a sour, green citrus fruit"

# print(fruit["lemon"])
# print(fruit["grape"])
#
# fruit['lime'] = "great with tequila"
#
# for snack in fruit:
#     print(snack + ": " + fruit[snack])

# while True:
#     shelf_key = input("Please enter a fruit: ")
#     if shelf_key == "quit":
#         break
#
#     description = fruit.get(shelf_key, "We don't have a " + shelf_key)   # this gets the description of a key
#     print(description)

###############
# Another Way #
###############

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#
#     if dict_key in fruit:
#         description = fruit[dict_key]         # this gets the description of a key
#         print(description)
#     else:
#         print("We don't have a " + dict_key)

################################
# Below is printing the shelve #
################################

# for f in fruit:
#     print(f + " - " + fruit[f])

#####################################
# Below is printing a sorted shelve #
#####################################

# ordered_keys = list(fruit.keys())
# # ordered_keys.sort()
# #
# # for f in ordered_keys:
# #     print(f + " - " + fruit[f])


#############################################
# Below is using items and values in shelve #
#############################################
# once the views are creates it will remain same unless it is converted to dictionary
# ** shelves can only have a string key unlike dictionary

for v in fruit.values():
    print(v)

print(fruit.values())

for f in fruit .items():
    print(f)

print(fruit.items())

fruit.close()                     # this is required as with is not used

# print(fruit)     # this is printing out a closed shelf
