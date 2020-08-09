from nested_data import albums    # this will execute the entire code in the file nested_data
# in order to avoid that we commented out everything in nested_data file

SONGS_LIST_INDEX = 3            # this is a constant in python, always in upper case
SONG_TITLE_INDEX = 1

while True:
    print("Please chose your album (invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):  # this is unpacking in the same line
        print("{}: {}".format(index + 1, title))
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        break

    print("Please choose your song:")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(track_number, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
    else:
        # break
        print("Please choose a valid option")    # these two lines is the challenge solution
        continue

    print("Playing {}".format(title))
    print("=" * 40)
