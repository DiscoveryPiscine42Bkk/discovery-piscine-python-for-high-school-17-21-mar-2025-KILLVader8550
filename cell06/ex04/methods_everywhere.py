#!/usr/bin/env python3 

import sys

def shrink(text):
    print(text[:7])

def enlarge(text):
    print(text + "Z"*(8 - len(text)))

if (len(sys.argv) < 1):
    print("none")
else:
    for i in sys.argv[1:]:
        if len(i) > 8:
            shrink(i)
        if len(i) < 8:
            enlarge(i)
        if len(i) == 8:
            print(i)