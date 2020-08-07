shopping_list = ["Sugar",
                 "Milk",
                 "Pasta",
                 "Spam",
                 "Eggs",
                 "Bread"
                 ]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]  # this is appending a member in the list
print(shopping_list)
print(id(shopping_list))
print(another_list)

a = b = c = d = e = f = another_list  # all the variables will bind to another_list
print(a)

print("Adding Cream")
b.append("cream")
print(c)
print(d)
