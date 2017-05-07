#!/usr/bin/env python3

import re
import requests
import sys

thing = sys.argv[1]
url = 'https://en.wikipedia.org/w/index.php?title=List_of_' + thing.replace(' ','_') + '&action=raw'

r = requests.get(url)
if r.status_code != 200:
    print("Error %s getting page" % str(r.status_code))
    sys.exit(1)

count = 0
for line in r.text.split('\n'):
    if line.startswith('* [[') or line.startswith('*[['):
       result = re.search('\\[\\[(.*?)\\]\\]', line)
       if not result:
           continue
       out_text = result.groups(0)[0].strip()
       if '|' in out_text:
           out_text = out_text.split('|')[1].strip()
       if out_text:
           count += 1
           print(out_text)

