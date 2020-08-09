# t = ("a", "b", "c")  # tuples are defined in parenthesis, if not parenthesis that's as well
# print(t)

# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the Lightning", "Metallica", 1984
#
# title, artist, year = metallica  # this is unpacking a tuple
# print(title)
# print(artist)
# print(year)
#
# table = ("Coffee table", 200, 100, 75, 34.50)
# print(table[1] * table[2])
#
# # It is very difficult to use above way of accessing the values of a tuple when you have large data
# # Unpacking tuple is always a better option to access the values in the tuple
#
# name, length, width, height, price = table
# print(length * width)  # in this case we don't care about the position of length and width in the tuple

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# # metallica[0] = "Masters of Puppets"  # this line will give an error, as tuples are immutable
#
# metallica2 = list(metallica)  # this is creating a list from the tuple metallica
# print(metallica2)
#
# metallica2[0] = "Master of Puppets"
# print(metallica2)
#
# metallica3 = tuple(metallica2)
# print(metallica3)


albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

print(len(albums))

# Tuples contains heterogeneous data i.e. different types such as int and char

# for album in albums:
#     print("Album: {}, Artist: {}, Year: {}"
#           .format(album[0], album[1], album[2]))

for name, artist, year in albums:                    # this is unpacking a tuple
    print("Album: {}, Artist: {}, Year: {}"          # this is more efficient way than the below example
          .format(name, artist, year))

for album in albums:
    name, artist, year = album                       # this is unpacking a tuple
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))
