shopping_list = ["Sugar", "Milk", "Pasta", "Spam", "Eggs", "Bread"]

item_to_find = "Yogurt"
found_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

# below 2 lines are same as above commented code but is more efficient of writing a python code

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is None:
    print("Item not found in the list")
else:
    print("The item is found at {} place".format(index))
    print(f"The item is found at {index} place")
