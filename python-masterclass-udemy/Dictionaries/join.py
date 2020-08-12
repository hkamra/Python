myList = ["a", "b", "c", "d"]
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "123456789"

newString = ''

# for c in myList:
#     newString += c + ", "        # inefficient way of joining the string
#
# print(newString)

# OR OR OR OR OR OR

# newString = ", ".join(myList)     # this is efficient way, and join doesn't need a loop
# print(newString)

# ------------------------------------------------------------------------------

# newString = ", ".join(letters)
# print(newString)

newString = " mississippi ".join(numbers)
print(newString)



