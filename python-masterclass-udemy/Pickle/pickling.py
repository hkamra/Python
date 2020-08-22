# this is serialization of data, saving of data is easy

import pickle

# imelda = ('More Mayhem',
#           'Imelda May',
#           '2011',
#           ((1, 'Pulling the Rug'),
#            (2, 'Psycho'),
#            (3, 'Mayhem'),
#            (4, 'Kentish Town Waltz')))
#
# with open("imelda.pickle", 'wb') as pickle_file:
#     pickle.dump(imelda, pickle_file)                  # this is writing to a file using pickle format


# with open("imelda.pickle", 'rb') as imelda_pickled:
#     imelda2 = pickle.load(imelda_pickled)                  # this is reading from a file using pickle format
#
# print(imelda2)
#
# album, artist, year, track_list = imelda2
#
# print(album)
# print(artist)
# print(year)
# for track in track_list:
#     track_number, track_title = track
#     print(track_number, track_title)


# imelda = ('More Mayhem',
#           'Imelda May',
#           '2011',
#           ((1, 'Pulling the Rug'),
#            (2, 'Psycho'),
#            (3, 'Mayhem'),
#            (4, 'Kentish Town Waltz')))
#
# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
#
# with open("imelda.pickle", 'wb') as pickle_file:
#     pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)    # this is writing to a file using pickle format
#     pickle.dump(even, pickle_file, protocol=0)                            # python has different version of protocols
#     pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)       # by default it uses version 3 protocol if we
#     pickle.dump(2998302, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)   # don't mention anything
#
# # unpickling only data that you trust as protocol versions are not audited
#
# with open("imelda.pickle", 'rb') as imelda_pickled:
#     imelda2 = pickle.load(imelda_pickled)                  # this is reading from a file using pickle format
#     even_list = pickle.load(imelda_pickled)
#     odd_list = pickle.load(imelda_pickled)
#     x = pickle.load(imelda_pickled)
#
# print(imelda2)
#
# album, artist, year, track_list = imelda2
#
# print(album)
# print(artist)
# print(year)
# for track in track_list:
#     track_number, track_title = track
#     print(track_number, track_title)
#
# print("=" * 40)
#
# for i in even_list:
#     print(i)
#
# print("=" * 40)
#
# for i in odd_list:
#     print(i)
#
# print("=" * 40)
#
# print(x)

# pickle.loads(b"cos\nsystem\n(S'rm imelda.pickle'\ntR.")     # Mac/Linux
pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR.")      # Windows, this is to delete the imelda.pickle file
