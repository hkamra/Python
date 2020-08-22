import shelve

with shelve.open('bike') as bike:
    bike['make'] = "Honda"                    # this is creating data in DB
    bike['model'] = "250 dream"
    bike['colour'] = "red"
    bike['engine_size'] = 250

    # del bike['engine_size']                 # this is to delete an entry from shelf same as dictionary

    for key in bike:
        print(key)

    print("=" * 40)

    print(bike["engine_size"])
    print(bike["colour"])
