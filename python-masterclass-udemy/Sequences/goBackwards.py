data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200

# working on a list backward is better as the index don't get messed up when the item is deleted
# from the list

# for index in range(len(data) - 1, -1, -1):
#     if data[index] < min_valid or data[index] > max_valid:
#         del data[index]
# print(data)

top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]

print(data)

