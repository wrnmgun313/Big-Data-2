#!/usr/local/bin/python3.9

# find top 4415

import sys

# top k
K = 4415
# review map
review_viewer = {}

# loop all record, get ufo and date
for line in sys.stdin:
    key, value = line.split( '\t' )
    ufo, date = value.split( ',' )
    review_viewer[key] = (ufo, date)

# sort by first ufo, then date
sorted_review = sorted(review_viewer.items(),key=lambda x:(x[1][0], x[1][1]),reverse=True)

# print all record, with limit k
for view in sorted_review[:K]:
  print(view[0] + '\t' + view[1][0])
