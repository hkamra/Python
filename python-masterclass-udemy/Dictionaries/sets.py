# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
#
# print("=" * 40)
#
# wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
# print(wild_animals)
#
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)

# empty_set = set()
# empty_set_2 = {}
# empty_set.add("a")
# # below line will give an error as line# 22 created a dictionary and add fx can't be used for sets
# # empty_set_2.add("a")
#
# even = set(range(0, 40, 2))   # this is called set constructor
# print(even)
# squares_tuple = {4, 6, 9, 16, 25}
# squares = set(squares_tuple)
# print(squares)

# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# squares_tuple = {4, 6, 9, 16, 25}
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))
#
# # below is the union operation in sets
#
# print(even.union(squares))
# print(len(even.union(squares)))
#
# print(squares.union(even))
#
# print("-" * 40)
#
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)

# even = set(range(0, 40, 2))
# print(sorted(even))
# squares_tuple = {4, 6, 9, 16, 25}
# squares = set(squares_tuple)
# print(sorted(squares))
#
# # a - b below is removing elements from a that are in b
# # b - a below is removing elements from b that are in a
#
# print("even minus squares")
# print(sorted(even.difference(squares)))  # either of this or below command can be used
# print(sorted(even - squares))
#
# print("squares minus even")
# print(sorted(squares.difference(even)))  # either of this or below command can be used
# print(sorted(squares - even))
#
# print("=" * 40)
#
# print(sorted(even))
# print(squares)
# even.difference_update(squares)  # this call will also remove elements from even that are in squares
# print(even)

even = set(range(0, 40, 2))
print(sorted(even))
squares_tuple = {4, 6, 9, 16, 25}
squares = set(squares_tuple)
print(sorted(squares))

# print("symmetric even minus squares")
# print(sorted(even.symmetric_difference(squares)))
#
# print("symmetric squares minus even")
# print(squares.symmetric_difference(even))  # this didn't require sorted but we can't rely on it

# below are the functions to remove or discard data from sets

# squares.discard(4)
# squares.remove(16)  # this will raise an error if the item is not in the set
# squares.discard(8)  # no error, does nothing
# print(squares)
# if 8 in squares:
#     squares.remove(8)   # this will raise an error if item is checked in the set before removing it
# try:
#     squares.remove(8)
# except KeyError:
#     print("The item 8 is not a member of the set")

# superset and subset

# if squares.issubset(even):
#     print("squares is a subset of even")
#
# if even.issuperset(squares):
#     print("even is a superset of squares")

# Frozen Set

even = frozenset(range(0, 100, 2))  # this set can be used as regular set but is immutable

print(even)
# even.add(3)  # this will give an error




