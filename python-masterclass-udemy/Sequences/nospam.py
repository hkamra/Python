menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# # my solution 1 (incorrect)
# for meal in menu:
#     for item in meal:
#         if item == "spam":
#             i = meal.index(item)
#             del meal[i]
#     print(meal)
#
# print(menu)


# my solution 2
for meal in menu:
    for index in range(len(meal) - 1, -1, -1):  # always delete the list in backward
        if meal[index] == "spam":
            del meal[index]

    print(", ".join(meal))

# print(menu)

# # another approach
# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item, end=" ")
#     print()

