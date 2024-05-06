#!/usr/local/bin/python3.9

import sys

# create month vector
monthList = [0]*12
# record size
sum = 0

# loop all record, and record month size
for line in sys.stdin:
    key, value = line.split( '\t' )
    monthList[int(key)-1] += 1
    sum+=1

# print all month and size
for idx, value in enumerate(monthList):
  print(str(idx+1)+'\t'+str(round(value*100.0/sum, 2))+'%')
