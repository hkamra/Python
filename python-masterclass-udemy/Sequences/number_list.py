empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# numbers = even + odd
# print(numbers)
#
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
# print(numbers)
#
# digits = sorted("432985617")  # sorted function always create a list, in this case list of strings
# digits_1 = list("432985617")  # list function prints out the same list
# print(digits)
# print(digits_1)
#
# # below are the methods of copying list
# # more_numbers = list(numbers)
# # more_numbers = numbers[:]
# more_numbers = numbers.copy()
#
# print(more_numbers)
# # more_numbers.append(12)
# # print(more_numbers)
# print(numbers is more_numbers)  # this verifies if the list is in the same order
# print(numbers == more_numbers)  # this verifies if the list contains same data



even.extend(odd)
print(even)

even.sort()
print(even)
another_even = even
print(another_even)

even.sort(reverse=True)  # sort changes the list and doesn't contain a new list
print(even)
print(another_even)




# print(min(even))
# print(min(odd))
# print(max(even))
# print(max(odd))
#
# print()
# print(len(even))
# print(len(odd))
#
# print()
# print("mississippi".count("s"))
# print("mississippi".count("iss"))
# print("mississippi".count("issi"))  # this shows that it will only go through the sequence once

