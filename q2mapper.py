#!/usr/local/bin/python3.9

import sys
import re
import json

# read from input
for line in sys.stdin:
  # parse json
  data = json.loads(line)
  # read yelping_since from json
  if 'yelping_since' in data:
    month = data['yelping_since'].split('-')[1]
    # print month as key, 1 as value
    print(month.strip() + "\t1")