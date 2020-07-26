a = 12
b = 3

print(a - b)   # 9
print(a + b)   # 15
print(a * b)   # 36
print(a / b)   # 4
print(a // b)  # for integer division, rounded down towards minus infinity
print(a % b)   # 0 modulo: the remainder after integer division

print()

for i in range(1, 4):
    print(i)

# for i in range(1, a / b):  # this will give error
#    print(i)

for i in range(1, a // b):  # this will give error
    print(i)


#  operator precedence PEMDAS, BEDMAS, BODMAS, BIDMAS

print()
print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print((((a + b) / 3) - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print()

print(a / (b * a) / b)



