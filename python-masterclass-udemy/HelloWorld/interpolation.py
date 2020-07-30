# string interpolation is only used in python 2

age = 24
print("My age is %d years" % age)
print("My age is %f years" % age)
print("My age is %s years" % age)

major = "years"
minor = "months"

print("My age is %d %s, %d %s" % (age, major, 6, minor))
print("PI is approx %f" % (22/7))
print("PI is approx %60.50f" % (22/7))  # 60 is width and 50 is precision
