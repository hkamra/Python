import shelve

# Run the code below without commenting such that the data is added to the DB
# and then we can add more data in the

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

# write back as True lets python waits for all the final updates to shelve data until the shelve is closed
# and in order to append data to the shelve list we don't have to write code from line 31 to 37

with shelve.open("recipes", writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans_on_toast"] = beans_on_toast
    # recipes["scrambled_eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup

    # below append calls won't add the data to the DB right away
    # unless we are using write back as True
    # recipes["blt"].append("butter")
    # recipes["pasta"].append("tomato")

    ######################################################
    # Below is the way to append data to the shelve list #
    ######################################################

    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list

    #######################################################
    # Below is the way to append using write back as True #
    #######################################################

    # recipes["soup"].append("croutons")       # this method is better than the below method

    ##################################################################
    # Below is the way to append a value in list and sync right away #
    ##################################################################

    # recipes["soup"] = soup
    # recipes.sync()
    # soup.append("cream")         # this value of cream is still in cache
    # soup.append("croutons")      # this value of cream is still in cache
    # recipes["soup"] = soup

    for snack in recipes:
        print(snack, recipes[snack])

