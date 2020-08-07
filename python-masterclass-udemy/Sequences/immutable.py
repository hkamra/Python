# result = True
# another_result = result
# print(id(result))    # id is used to get the memory address
# print(id(another_result))
#
# result = False    # false is assigned/bound to a new variable
# print(id(result))

result = "Correct"
another_result = result
print(id(result))    # id is used to get the memory address
print(id(another_result))

result += "ish"
print(id(result))

