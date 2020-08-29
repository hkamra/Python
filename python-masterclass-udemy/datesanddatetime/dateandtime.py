# import time
#
# # NOTE:- object has different directives, refer to the time and conversion document
# # if the second parameter is not used, it will be localtime by default
#
# print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))
#
# print("The current time zone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))
#
# if time.daylight != 0:
#     print("\tDaylight Saving Time is in effect for this location")
#     print("\tThe DST timezone is " + time.tzname[1])
#
# print("Local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# print("UTC time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))

import datetime

print(datetime.datetime.today())   # first datetime in this call is a module and second one is a class
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
