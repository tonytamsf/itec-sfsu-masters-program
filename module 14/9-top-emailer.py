#!/usr/bin/env python3
#
# Tony Tam (c) May 9, 2023 - https://github.com/tonytamsf
# 
##############################
# https://www.py4e.com/tools/pythonauto/?PHPSESSID=08239d7c68c700c9849d28c94d6c44c1
# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

senders = {}
handle = open(name)
for line in handle:
  if (not line.startswith("From ")):
      continue
  sender = line.split()[1]
  if (not sender in senders):
      senders[sender] = 1
  else:
      senders[sender] = senders[sender] + 1

max_sender = None
for sender in senders:
   if (not max_sender == None):
      if (senders[max_sender] < senders[sender]):
          max_sender = sender
   else:
       max_sender = sender          

print(max_sender, senders[max_sender])
handle.close()
