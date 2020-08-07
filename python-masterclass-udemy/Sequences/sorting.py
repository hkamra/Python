#

pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)  # this function always returns a list in alphabetical order
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)  # this created a new list
print(sorted_numbers)
print(numbers)

another_sorted_numbers = numbers.sort()   # this sorted the same list, we should not use variable to assign this
print(numbers)
print(another_sorted_numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold)  # this is not a pangram, using casefold like this will make case insensitive
print(missing_letter)

names = ["Graham", "John", "Terry", "Eric", "terry", "michael"]

names.sort(key=str.casefold)
print(names)
