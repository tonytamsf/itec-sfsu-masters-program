#!/usr/bin/env python3

# https://www.py4e.com/tools/pythonauto/?PHPSESSID=9f9b7d4f4b3482d01d3af644ef68bd45
# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total_confidence = 0;
count = 0;

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    confidence = float(line[line.rfind(" "):])
    total_confidence = total_confidence + confidence;
    count = count + 1
    running_avg = total_confidence / count
    #print(running_avg)

print("Average spam confidence:", running_avg)

fh.close()
