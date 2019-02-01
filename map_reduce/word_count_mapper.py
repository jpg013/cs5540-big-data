#!/usr/bin/env python

import sys

key_mapper = lambda x: x.strip().lower()
key_filter = lambda x: len(x) > 0

for line in sys.stdin:  
    line = line.strip()
    tokens = list(map(key_mapper, line.split()))
    keys = list(filter(key_filter, tokens))
    
    for key in keys: 
        print('{0}\t{1}'.format(key, 1) )
