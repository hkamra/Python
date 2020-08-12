locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

Vocabulary = {"quit": "Q",
         "east":  "E",
         "south": "S",
         "west":  "W",
         "north": "N",
         "QUIT":  "Q",
         "EAST":  "E",
         "SOUTH": "S",
         "WEST":  "W",
         "NORTH": "N"}

loc = 1

while True:
    # availableExits = ""
    # for direction in exits[loc].keys():   # this is retrieving the keys in a dictionaries within a list
    #     availableExits += direction + ", "

    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + availableExits + " ").upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        for word in Vocabulary.keys():
            if direction == word:
                direction = Vocabulary.get(word)
                if direction in exits[loc]:
                    loc = exits[loc][direction]
                break
        else:
            print("You cannot go in that direction")
