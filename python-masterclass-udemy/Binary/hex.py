# for i in range(17):
#     print("{0:>2} in binary is {0:08x}".format(i))
#
# x = 0x20
# y = 0x0A
# print("{0:08x}".format(x * y))

# below code converts the decimal to binary

# print("Please enter the decimal number between 1 to 65535: ")
# user_input = int(input())
# rem = 0
# a = 1
# num = 0
#
# while user_input != 0:
#     rem = user_input % 2
#     num = num + (rem * a)
#     user_input //= 2
#     a = a * 10
#
# print(num)

# Tim's solution
# below is cool way of finding a binary

powers = []
for power in range(15, -1, -1):
    powers.append(2 ** power)
print(powers)

x = int(input("Please enter a number: "))

printing = False

for power in powers:
    bit = x // power
    if bit != 0 or power == 1:
        printing = True
    if printing:
        print(bit, end='')
    x %= power
