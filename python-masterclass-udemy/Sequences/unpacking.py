a = b = c = d = e = f = 42  # all the variables are bind to the same value 42
print(c)

x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

print("unpacking a tuple")

data = 1, 2, 76  # data represents a tuple
x, y, z = data  # this is unpacking a tuple
print(x)
print(y)
print(z)

print("unpacking a list")

data_list = [12, 13, 14]
data_list.append(15)

p, q, r = data_list  # this is unpacking a list
print(p)
print(q)
print(r)

