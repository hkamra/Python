fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour yellow, citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

veg = {"cabbage": "every child's favourite",
       "sprouts": "mmmm, lovely",
       "spinach": "can I have some more fruit, please"}

print(veg)

# below is the method to combine two dictionaries

# veg.update(fruit)     # this can also be done other way fruit.update(veg)
# print(veg)
#
# fruit.update(veg)    # this modifies the original dictionary
# print(fruit)

# if we want to create a new dictionary, we can do so using below method

nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)
print(veg)
print(fruit)

