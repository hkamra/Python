# dictionaries and key can't be access using the index as they are unordered
# .key() - obtain key    .get() - get the description of the key

fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour yellow, citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
#         "apple": "round and crunchy"   # this value will override the previous value of the key

# print(fruit)
# print(fruit["lemon"])  # this is a syntax for accessing the definition using a key
#
# fruit["pear"] = "an odd shaped apple"   # each key is unique in dictionary
# print(fruit)
# fruit["lime"] = "great with tequila"
# print(fruit)
#
# # del fruit["lemon"]   # this will delete the key "lemon" from the dictionary
# # print(fruit)
# #
# # # del fruit   # this command will delete the entirely dictionary
# #
# # fruit.clear()   # this will clear the entire dictionary
# # print(fruit)
#
# print(fruit["tomato"])

print(fruit)

# below is adding an object in the dictionary

# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)


# ------------------------------------------------------------------------------
# below is another method to retrieve the key and the description using .item() object

print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print(dict(f_tuple))

# ------------------------------------------------------------------------------

# ordered_keys = list(fruit.keys())
# ordered_keys = sorted(list(fruit.keys()))
# ordered_keys.sort()
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

# OR OR OR OR OR

# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])

# for val in fruit.values():
#     print(val)
#
# for keys in fruit.keys():   # this is more efficient way
#     print(keys)

# ------------------------------------------------------------------------------


# when printing a dictionary, the order might change how python stores data in memory

# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print('-' * 40)

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We don't have a " + dict_key)
#     fruit.has_key(dict_key)   #  this is a python 2 function and has been deprecated from python 3
#     print(description)
#     if dict_key in fruit:
#         description = fruit.get(dict_key)  # this is to get the description of the key
#         print(description)
#     else:
#         print("We don't have a " + dict_key)

# for snack in fruit:
#     print(fruit[snack])
