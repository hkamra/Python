
shopping_list = ["Sugar", "Milk", "Pasta", "Spam", "Eggs", "Bread"]

# for item in shopping_list:
#     if item != "Spam":
#         print(item)

for item in shopping_list:
    if item == "Spam":
        continue
    else:
        print("Buy " + item)

print("\n\n\n")

for item in shopping_list:
    if item == "Spam":
        break
    else:
        print("Buy " + item)

