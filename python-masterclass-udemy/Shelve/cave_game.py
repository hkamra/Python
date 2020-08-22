# from cave_initialise import shelve_1
# from cave_initialise import shelve_2
import shelve

shelve_1 = shelve.open("locations")
shelve_2 = shelve.open("vocabulary")

loc = "1"
while True:
    availableExits = ", ".join(shelve_1["locations"][loc]["exits"].keys())

    print(shelve_1["locations"][loc]["desc"])

    if loc == "0":
        break
    else:
        allExits = shelve_1["locations"][loc]["exits"].copy()
        allExits.update(shelve_1["locations"][loc]["namedExits"])

    direction = input("Available exits are " + availableExits + " ").upper()
    print()

    # Parse the user input, using our vocabulary dictionary if necessary
    if len(direction) > 1:  # more than 1 letter, so check vocab
        words = direction.split()
        for word in words:
            if word in shelve_2["vocabulary"]:   # does it contain a word we know?
                direction = shelve_2["vocabulary"][word]
                break

    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cannot go in that direction")

shelve_1.close()
shelve_2.close()
