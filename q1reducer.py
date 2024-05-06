#!/usr/local/bin/python3.9

import sys

# previous cate
previous = None
# cate related business ids
pre_bus_ids = []

# read from mapper output, sorted by cate
for line in sys.stdin:
    key, value = line.split( '\t' )
    # if meet next cate
    if key != previous:
        # print all business id
        if previous is not None:
            print(previous + '\t' + '[ ' + ','.join(pre_bus_ids) + ' ]')
        # set previous as current cate
        previous = key
        pre_bus_ids = []
    pre_bus_ids.append(value.strip())
    
# print last cate
print(previous + '\t' + '[ ' + ','.join(pre_bus_ids) + ' ]')