parrot = "Norwegian Blue"

print(parrot)
str_length = len(parrot)

#  below is a min challenge to print "We Win" using indexing
print(parrot[3].upper())
print(parrot[4])
print(parrot[9])
print(parrot[3].upper())
print(parrot[6])
print(parrot[8])

print()

#  below is the example of negative indexing, a mini challenge to print "We Win" using negative indexing
# the logic to find the negative indexing is (positive index - string length)

print(parrot[-11].upper())
print(parrot[-10])
print(parrot[-5])
print(parrot[-11].upper())
print(parrot[-8])
print(parrot[-6])

print()

print(parrot[3 - str_length].upper())
print(parrot[4 - str_length])
print(parrot[9 - str_length])
print(parrot[3 - str_length].upper())
print(parrot[6 - str_length])
print(parrot[8 - str_length])

#  below is called slicing

print()

print(parrot[0:6])  # note this is up to but not including index 6
print(parrot[3:5])  # note this is up to but not including index 5
print(parrot[0:9])  # note this is up to but not including index 9
print(parrot[:9])   # note this is up to but not including index 9
print(parrot[10:14])
print(parrot[10:])  # this will assume the default stop value

print()

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])

print(parrot[:])   # this is very important

# below is slicing using negative indexing
print("negative slicing")

print(parrot[-4:2])  # this won't print anything because the start cannot be lower than the stop

print(parrot[-14:-8])
print(parrot[-4:12])

# below is step in slicing
print("\n\n\n")
print(parrot[0:6:2])  # Nre, the third digit is for stepping. Print every second alphabet
print(parrot[0:6:3])  # Nw

print()

number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])


