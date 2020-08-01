age = int(input("How old are you? "))

# if age >= 16 & age <= 65:
# below is an example of simplified chained comparison

# if 16 <= age <= 65:

if age in range(16, 66):
    print("Have a good day at work")
else:
    print("Enjoy your free time.")

print("-" * 80)

if age < 16 | age > 65:
    print("Enjoy your free time.")
else:
    print("Have a good day at work")

