#!/usr/bin/env python3
from time import localtime, mktime, strftime

start_time = localtime()
print(f'Timer started at {strftime("%X", start_time)}')

input('Press "Enter" to stop timer ')

stop_time = localtime()
difference = mktime(stop_time) - mktime(start_time)

print(f'Timer stopped at {strftime("%X", stop_time)}')
print(f'Total time: {difference} second(s)')
