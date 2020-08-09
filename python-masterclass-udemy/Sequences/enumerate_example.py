# for index, character in enumerate("abcdefgh"):
#     print(index, character)

for t in enumerate("abcdefgh"):  # this is unpacking a tuple
    index, character = t
    print(index, character)

index, character = (0, 'a')
print(index)
print(character)
