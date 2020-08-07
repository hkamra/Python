user_string = "-"
print("Enter the string: ")
user_string = input()
len_user_string = len(user_string)
characters_list = []

len_string = 0
a = 0

while a != len_user_string:
    for i in range(a, len_user_string):
        if user_string[i] not in characters_list:
            characters_list.append(user_string[i])

            if (i == len(user_string) - 1) and (len(characters_list) > len_string):
                len_string = len(characters_list)
        else:
            if len(characters_list) > len_string:
                len_string = len(characters_list)
            characters_list.clear()
            a += 1
            break

# characters_list.sort(key=str.casefold)
# print(characters_list)
# print(len(characters_list))
print(len_string)


# characters_list = []
#
# len_string = 0
#
# for char in user_string:
#     if char not in characters_list:
#         characters_list.append(char)
#
#         if user_string.index(char) == len(user_string) - 1:
#             len_string = len(characters_list)
#     else:
#         if len(characters_list) > len_string:
#             len_string = len(characters_list)
#         characters_list.clear()
#         characters_list.append(char)
#
# # characters_list.sort(key=str.casefold)
# # print(characters_list)
# # print(len(characters_list))
# print(len_string)

