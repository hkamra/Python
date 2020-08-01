quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.

for char in quote:
    if char.isupper():
        print(char)

for i in range(0, 100, 7):
    print(i)
    if (i % 11) == 0 and i != 0:
        break

for i in range(0, 21):
    if (i != 0) and ((i % 3 == 0) or (i % 5 == 0)):
        continue
    elif i != 0:
        print(i)


