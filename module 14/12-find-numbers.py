#!/usr/bin/env python3
#
# Tony Tam (c) May 9, 2023 - https://github.com/tonytamsf
# 
##############################
# https://www.py4e.com/tools/python-data/?PHPSESSID=9eeef295b83f8cdfde5254b63fb25f26
# Welcome Tony Tam from Python for Everybody
# 
# Finding Numbers in a Haystack
# 
# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
# 
# Data Files
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
# 
# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_1811342.txt (There are 79 values and the sum ends with 27)
# These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.
#

import re
filename = input("Filename:")
if (len(filename) < 1):
    filename = "regex_sum_42.txt"

re_numbers = '(\d+)'
total_sum = 0
handle = open(filename)
for line in handle:
    numbers = re.findall(re_numbers, line)
    if (len(numbers) > 0):
        total_sum = total_sum + sum([ int(x) for x in numbers ])

print(total_sum)
handle.close()
