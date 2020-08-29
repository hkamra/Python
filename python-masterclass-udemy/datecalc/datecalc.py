import time

# Python Enhancement Proposal - PEP

# print(time.gmtime(0))
#
# print(time.localtime(time.time()))
#
# print(time.time())   # this is the time when epoch started i.e. 1970
#
# time_here = time.localtime()
# print(time_here)
# print("Year:", time_here[0], time_here.tm_year)
# print("Month:", time_here[1], time_here.tm_mon)
# print("Day:", time_here[2], time_here.tm_mday)

# from time import time as my_timer
from time import perf_counter as my_timer    # this doesn't give the system time. This is best
# from time import monotonic as my_timer
# from time import process_time as my_timer      # this shows the CPU processing time
import random

input("Press enter to start ")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()                   # this function returns the system time at that instant
input("Press enter to stop ")

end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))    # strftime returns the local time
print("Ended at " + time.strftime("%X", time.localtime(end_time)))        # %X lower and upper case makes a diff

print("Your reaction time was {} seconds".format(end_time - start_time))
