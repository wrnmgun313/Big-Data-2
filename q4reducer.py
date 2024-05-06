#!/usr/local/bin/python3.9

import sys
import string
import random

# all avaiable characters
allowed_chars = string.ascii_letters + '0123456789_-'

# random function
def random_string_generator(str_size):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

# previous name and date list
previous = None
date_list = []
buss_name = None
for line in sys.stdin:
    key, value = line.split( '\t' )
    if key != previous:
        # meet new business id, print previous
        if previous is not None and buss_name is not None:
            # loop all date
            for dates in date_list:
              date_ss = dates.split(',')
              for data in date_ss:
                # print uid, date, buss_name
                print(random_string_generator(22) + '\t' + data + '\t' + str(buss_name))
        previous = key
        date_list = []
        buss_name = None
    arr = value.split(',')
    val = value[2:]
    if (arr[0].strip() == '1'):
      buss_name = val
    else:
      date_list.append(val)

# print last one
if previous is not None and buss_name is not None:
  for dates in date_list:
    date_ss = dates.split(',')
    for data in date_ss:
      print(random_string_generator(22) + '\t' + data + '\t' + buss_name)