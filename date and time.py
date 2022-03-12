""" The Time module - begins recording time from the epoch that begins at 00.00.00,1st Jan 1970"""
# time() - returns the number of seconds
# ctime() - returns the current date and time
# sleep() - stops execution of a thread for the given duration
# localtime() - returns the dates and time in time.struct-time format
# gmtime() - returns time.struct_time in UTC format
# mktime() - returns the seconds passed since epoch pas output
# asctime() - returns a string representing the same

import time
print(time.time())  # Returns the number of seconds that have passed since Epoch
print(time.ctime(1618919357.7818708))
help(time.time)
print(time.localtime())

import time
a=time.localtime()   # storing the localtime in a variable
b=time.mktime(a)     # pass the parameter to it
print(b)     # returns the number of seconds that have passed since the epoch time till now
c=time.asctime(a)  # fetching the current date and time from the struct time format into the local format
print(c)

help(time.strftime)
import time
x = time.strftime("%m/%d/%Y")
print(x)
y="08 August 2019"
s = time.strptime(y,"%d %B %Y")   # changing into struct time format
print(s)


""" Date time module """
# datetime()- datetime constructor
# datetime.today() - returns the current date and time
# datetime.now() - returns the current date and time
# date() - takes year,month and day as parameter and creates the corresponding date
# time() - takes hour,min sec,microseconds and tzinfo as parameter and creates the corresponding time
# datetime.fromstamp() - converts seconds to return the corresponding date and time
# timedelta() - difference between dates or time(duration)

import datetime
print(datetime.datetime(2020,5,4,13,8,56))
print(datetime.datetime.today())
print(datetime.datetime.now())

# accessing a particular attribute
import datetime
v = datetime.datetime.now()
print(v.year)
b1 = datetime.timedelta(days=20)
b2 = datetime.timedelta(days=30)
b3 = b1-b2
print(b3)
print(type(b3))
