#!/usr/local/bin/python3.9

import sys
import re
import json

# read from input
for line in sys.stdin:
  # parse json
  data = json.loads(line)
  if 'name' in data:
    # business data
    # print business_id as key, name as value
    print(data['business_id'].strip() + '\t1,' + data['name'].strip())
  else:
    # checkin data
    # print business_id as key, date as value
    print(data['business_id'].strip() + '\t2,'+ data['date'].strip())