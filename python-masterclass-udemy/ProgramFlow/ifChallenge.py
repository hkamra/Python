name = input("Please enter your name? ")
age = int(input("{}, please enter your age: ".format(name)))

if 18 <= age < 31:
    print("{}, you are welcome on this holiday trip!".format(name))
else:
    print("{}, sorry you are not allowed on this holiday trip".format(name))

