for i in range(1, 13):
    print("No. {:2} squared is {:3} and cubed is {:4}".format(i, i ** 2, i ** 3))  # ** is same as power
print("*" * 80)

print()


name = input("Please enter your name: ")
age = input("How old are you, {0}? ".format(name))
print(age)
print(f"Himanshu is {age} years old.")

age = int(age)

if (age >= 18) & (age < 900):
    print("You are old enough to vote.")
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("You come back in {0} years.".format(18 - age))





