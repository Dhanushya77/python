#built in module-
import datetime
print(datetime.datetime.now())
print(datetime.datetime.now().strftime('%x'))   # 	Local version of date
print(datetime.datetime.now().strftime('%X'))   # 	Local version of time
print(datetime.datetime.now().strftime('%A'))   # 	Weekday, full version
print(datetime.datetime.now().strftime('%a'))   #  Weekday, short version
print(datetime.datetime.now().strftime('%m'))   #  Month as a number 01-12
print(datetime.datetime.now().strftime('%W'))   #  Week number of year, Monday as the first day of week, 00-53
print(datetime.datetime.now().strftime('%w'))   #  Weekday as a number 0-6, 0 is Sunday
print(datetime.datetime.now().strftime('%d'))   #  Day of month 01-31
print(datetime.datetime.now().strftime('%y'))   #  Year, short version, without century
print(datetime.datetime.now().strftime('%Y'))   #  Year, full version
print(datetime.datetime.now().strftime('%c'))   #  Local version of date and time
print(datetime.datetime.now().strftime('%p'))   #  AM/PM
print(datetime.datetime.now().strftime('%b'))   #  Month name, short version
print(datetime.datetime.now().strftime('%B'))   #  Month name, full version
print(datetime.datetime.now().strftime('%j'))   #  Day number of year 001-366

#built in module-math
import math
print(math.factorial(5))        #  factorial
print(math.sqrt(25))            #  square root
print(math.ceil(12.5))          #  round to upper
print(math.floor(12.5))         #  round to lower