for i in range(1, 13):
    print("No. {0:2} squared {1:3} and cubed is {2:4}.".format(i, i ** 2, i ** 3))

#  second digit in the replacement above indicates the width of replacement field

print()

for i in range(1, 13):
    print("No. {0:>2} squared {1:<3} and cubed is {2:^4}.".format(i, i ** 2, i ** 3))

#  < is left aligned, nothing or > will be right aligned, and ^ will be centre aligned

print()

print("Pi is approx {0:12}".format(22 / 7))
print("Pi is approx {0:12f}".format(22 / 7))
print("Pi is approx {0:12.50f}".format(22 / 7))  #  width is ignored due to floating
print("Pi is approx {0:12.50f}".format(22 / 7))
print("Pi is approx {0:62.50f}".format(22 / 7))
print("Pi is approx {0:72.50f}".format(22 / 7))

for i in range(1, 13):
    print("No. {} squared {} and cubed is {:4}.".format(i, i ** 2, i ** 3))

