# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import datetime
from typing import List, Any, Union

import pytz

nine_timezones = []
i = 0
max_number_tzs = 9

# in case of new list, always use either append or insert
# below is my solution, I have created a list from first 9 TZs

for x in pytz.all_timezones:
    if i != 9:
        nine_timezones.append(x)
        i += 1
    else:
        break

while True:
    i = 1
    for x in nine_timezones:
        print(str(i) + ": " + x)
        i += 1
    user_input = int(input("\nPlease select one of the following timezones from the above TZs: "))

    print()

# ** strftime() is very useful to display time and date in format suitable for user to read

    if user_input < max_number_tzs and user_input != 0:
        user_input -= 1
        tz_to_display = pytz.timezone(nine_timezones[user_input])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print("The time in {} is {} {}".format(nine_timezones[user_input], world_time.strftime('%A %x %X %z'), world_time.tzname()))
        print("Local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
        print("The UTC time is {}\n".format(datetime.datetime.utcnow().strftime('%A %x %X')))
    else:
        break




