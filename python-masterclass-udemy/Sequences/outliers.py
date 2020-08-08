# data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 350, 360]
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160]
# data = [104, 105, 110, 120, 130, 130, 150, 160, 350, 360]
# data = [104, 105, 110, 120, 130, 130, 150, 160]
# data = [1401, 1402, 1511, 1265, 1356]
data = []

# above ar different test cases to test that the below code works fine

data.sort()  # this will make the below code works even if the list is not sorted

min_valid = 100
max_valid = 200

# process the low values in the list

stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)  # for debugging, this is the index of the value greater in the list
del data[:stop]
print(data)

# process the high values in the list
start = 0
for index in range(len(data) - 1, -1, -1):  # -1 is to include value at index 0, and stepping -1 for backward
    if data[index] <= max_valid:
        start = index + 1
        break

print(start)
del data[start:]
print(data)

# del data[0:2]
# print(data)
# del data[9:]
# print(data)

# note, don't modify loop control variable in python during iteration i.e. index in below case

# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index]
#
# print(data)
