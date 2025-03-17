#!/usr/bin/env python3

import sys

result = list(sys.argv[1])

count = 0

for i in range (len(result)):
    if (result[i] == 'z'):
        count += 1 
    else:
        pass

if (count != 0):
    print("z"*count)
else:
    print("None")