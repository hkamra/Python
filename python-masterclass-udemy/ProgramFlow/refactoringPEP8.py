# below code has been taken from escape char file from Hello world project

split_string = "This string has been \nsplit over\nseveral\nlines"
print(split_string)

tabbed_string = "1\t2\t3\t4\t5"
print(tabbed_string)  # the gap between the above characters are defined in the IDE by default

print('The pet shop owner said "No, no, \'e\' uh,...he\'s resting".')
# or
print("The pet shop owner said \"No, no, \'e\' uh,...he\'s resting\".")

print("""The pet shop owner said "No, no, 'e' uh,...he's resting".""")

another_split_string = """This string has been
split over
several
lines"""

print(another_split_string)

# below code shows the use of escape character
another_split_string = """This string has been \
split over \
several \
lines"""

print(another_split_string)

print("C:\\Users\\tim\\notes.txt")  # prefer to use this method
print(r"C:\Users\tim\notes.txt")

