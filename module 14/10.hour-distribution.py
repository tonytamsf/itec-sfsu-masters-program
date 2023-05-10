#!/usr/bin/env python3
#
# Tony Tam (c) May 9, 2023 - https://github.com/tonytamsf
# 
##############################
# https://www.py4e.com/tools/pythonauto/?PHPSESSID=df4ca2c157692a1517738972ef82fed5
# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)
hour_count = dict()
for line in handle:
    if (not line.startswith('From ')):
        continue
    words = line.split()
    time = words[5]
    hour = time.split(':')[0]
    #print(hour)
    hour_count[hour] = hour_count.get(hour,0) + 1

sorted_list = list(hour_count.items())
sorted_list.sort()
for key, val in sorted_list:
    print(key, val)
handle.close()