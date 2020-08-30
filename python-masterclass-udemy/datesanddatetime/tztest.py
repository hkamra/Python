import pytz
import datetime

country = 'Asia/Kolkata'

# tz_to_display = pytz.timezone(country)
# local_time = datetime.datetime.now(tz=tz_to_display)
# print("The time in {} is {}".format(country, local_time))
# print("UTC is {}".format(datetime.datetime.utcnow()))

# for x in pytz.all_timezones:
#     print(x)
#
# for x in sorted(pytz.country_names):
#     print(x + ": " + pytz.country_names[x])

# below code displays all the time zones for all the countries in pytz
# if the country does not have the time zone it will give an error
# using get function below will avoid the error, if the return is none it will be handled by get function
# for x in sorted(pytz.country_names):
#     # print("{}: {}: {}:".format(x, pytz.country_names[x], pytz.country_timezones[x]))
#     print("{}: {}: {}:".format(x, pytz.country_names[x], pytz.country_timezones.get(x)))


# below code is another way of printing the time zones except if the time zone does not exist it will display
# a message

for x in sorted(pytz.country_names):
    print("{}: {}:".format(x, pytz.country_names[x]), end=": ")
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
        # print(pytz.country_timezones[x])      # this is the list of timezones in pytz
    else:
        print("\t\tNo time zone defined")

