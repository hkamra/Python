computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]

print(computer_parts)

# computer_parts[3] = "trackball"
print(computer_parts[3:])

# computer_parts[3:] = "trackball"  # this will add the item of the string in the list individually i.e. iterable
# In order to fix above problem, put the above string in the list
computer_parts[3:] = ["trackball"]
print(computer_parts)



# for part in computer_parts:
#     print(part)
#
# print()
#
# print(computer_parts[2])
#
# print(computer_parts[0:3])  # slicing a list produces another list as shown in the output
# print(computer_parts[-1])

