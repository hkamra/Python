panagram = """The quick brown
fox jumps\tover
the lazy dog"""

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

# values = "".join(char if char not in separators else " " for char in numbers).split()
generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']
values = "".join(generated_list)  # join creates a string
print(values)

values_list = values.split()  # split converts a string into a list
print(values_list)

# Use a for loop to produce a list of ints, rather than strings.
# You can either modify the contents of the 'values_list' list in place,
# or create a new list of ints.

# method 1 updating the same list

for index, value in enumerate(values_list):
    values_list[index] = int(value)

print(values_list)

# # method 2 creating a new list
# new_list = []
#
# for i in range(0, len(values_list)):  # range(0, len(values_list)) should be written as range(len(values_list))
#     new_list.append(int(values_list[i]))
#
# print(new_list)
