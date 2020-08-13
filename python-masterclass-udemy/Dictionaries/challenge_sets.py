# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

# vowels_tuple = {"a", "e", "i", "o", "u"}
# vowels = set(vowels_tuple)
# user_input = input("Please enter the string ")
#
# formatted_input = set(user_input.lower())
# formatted_input.discard(" ")
# print(sorted(formatted_input))
# print(sorted(formatted_input.difference(vowels)))


# Below is Tim's Solution

sampleText = "Python is a very powerful language"

vowels = frozenset("aeiou")
# or vowels = {"a", "e", "i", "o", "u"}
finalSet = set(sampleText).difference(vowels)
print(finalSet)

finalList = sorted(finalSet)
print(finalList)
