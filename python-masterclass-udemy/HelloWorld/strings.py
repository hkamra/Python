print("Today is a good day to learn Python")
print("Python is fun")
print("Python's string are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " world")  # this is concatenation

greeting = "Hello"
name = "Himanshu"
print(greeting + name)

# if we want to add space, we can add that too
print(greeting + ' ' + name)

age = 24  # value 24 is bind to variable age
print(24)

print(type(greeting))  # this is to know the data type of the variable
print(type(age))

# age = "2 years"  # this functionality is only available in python, assigning a string value(rebound) to an integer
# print(type(age))

# terminology used in python is that a string hello is bound to variable greeting

# in order to improve and don't confuse the reader of the code

age_in_words = "2 years"
print(name + " is " + str(age) + " years old")
print(type(age))

