string = [None, 1, 2, 3, 4, 0]

exit_option_selected = False
# match_found = False

while True:  # always prefer to have a condition here to terminate while loop instead of using True
    option_selected = int(input(print("Please select from one of the following options:-\n1. 1\n2. 2\n3. 3\n4. 4\n5. 0")))

    for i in string:
        if option_selected == 0:
            print("You have chosen to exit")
            exit_option_selected = True
            break
        elif i == option_selected:
            index = string.index(i)
            print(f"You selected option {index}")
            # match_found = True
            break
    else:
        print("You have selected an invalid option, please select again")

    if exit_option_selected:  # or match_found:
        break
