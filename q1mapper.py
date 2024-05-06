#!/usr/local/bin/python3.9

import sys
import re
import json

# read from input
for line in sys.stdin:
  # parse json
  data = json.loads(line)
  # get categories and business_id
  if 'categories' in data and 'business_id' in data:
    bus_id = data['business_id'].strip()
    cates = data['categories'].split(',')
    # loop cate and print cate as key, business_id as value
    for cate in cates:
      print(cate.strip() + "\t" + bus_id)