#!/usr/bin/env python3
#
# Tony Tam (c) May 10, 2023 - https://github.com/tonytamsf
# 
##############################

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
times = input('How deep to go (4): ')
if (len(times) < 1):
    times = 4
else:
    times = int(times)

pos = input('What position do we start (3): ')
if (len(pos) < 1):
    pos = 3
else:
    pos = int(pos)



def follow_links(url, pos, times):
   html = urlopen(url, context=ctx).read()
   soup = BeautifulSoup(html, "html.parser")
    # Retrieve all of the anchor tags
   tags = soup('a')
   # Humans think with 1 as the start, but we start at zero
   tag = tags[pos - 1]
   # Look at the parts of a tag
   name = tag.contents[0]
   print(name)
   if (times == 1):
       return
   href = tag.get('href', None)
   follow_links(href, pos, times - 1)

follow_links(url, pos, times)