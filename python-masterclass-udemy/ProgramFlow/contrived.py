numbers = [1, 45, 31, 12, 60]

for number in numbers:
    if number % 8 == 0:
        # reject the list
        print("The numbers are unacceptable")
        break
else:           # this else is tied to for loop, in case numbers are not divisible by 8
    print("All those number are fine")

# code has been modified in the file hiLo.py to use above else statement
