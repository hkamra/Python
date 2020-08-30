import datetime
import pytz

# Note:- Always use UTC time in python and only use local time when you want to display the time

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Naive local time {}".format(local_time))
print("Naive UTC {}".format(utc_time))

aware_local_time = pytz.utc.localize(utc_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware local time {}, time zone {} ".format(aware_local_time, aware_local_time.tzinfo))
print("Aware UTC {}, time zone {} ".format(aware_utc_time, aware_utc_time.tzinfo))

gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)  # this is find the number of seconds since epoch
print(gap_time)
print(gap_time.timestamp())

s = 1445733000  # this seconds should be in UK
t = s + (60 * 60)   # this is increasing 1hr due to daylight saving time(DST)


# always use utcfromtimestamp

gb = pytz.timezone('GB')
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print("{} seconds since epoch is {}".format(s, dt1))
print("{} seconds since epoch is {}".format(t, dt2))
