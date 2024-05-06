#!/usr/local/bin/python3.9

import sys
import re
import json

# read from input
for line in sys.stdin:
  # parse json
  data = json.loads(line)
  # read review_id and date in json
  if 'review_id' in data and 'date' in data:
    review_id = data['review_id']
    # calculate ufo
    ufo = 0
    if 'useful' in data:
      ufo += data['useful']
    if 'funny' in data:
      ufo += data['funny']
    if 'cool' in data:
      ufo += data['cool']
    # print review_id as key, ufo+date as value, date used to sort order
    print(review_id.strip() + "\t" + str(ufo) + "," + data['date'])