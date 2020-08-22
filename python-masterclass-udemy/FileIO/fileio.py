# # jabber = open("H:\\Resources_Udemy\\Python_MasterClass\\156\\sample.txt", 'r')
# jabber = open("sample.txt", 'r')
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')  # this will not put the line ending character
#
# jabber.close()

# below is the python3 way using 'with' keyword which will handle the exception if there is any error reading the file
# below code doesn't require closing the file

# with open("sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()


# below code will store the entire text file as list
# with open("sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')

with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()             # reads the entire line and create list of strings
print(lines)

for line in lines[::-1]:
    print(line, end='')

with open("sample.txt", 'r') as jabber:
    lines = jabber.read()                 # reads the entire file
print(lines)

for line in lines[::-1]:
    print(line, end='')

