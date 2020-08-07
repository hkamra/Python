user_string = "-"
print("Enter the string: ")
user_string = input()

unique_chars = []

for char in user_string:
    if char not in unique_chars:
        unique_chars.append(char)
    else:
        continue

unique_chars.sort(key=str.casefold)
print(unique_chars)
print(len(unique_chars))
