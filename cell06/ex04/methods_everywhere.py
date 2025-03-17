#!/usr/bin/env python3 

import sys

def shrink(var):
    print(var[0:7])

def enlarge(var):
    print(var + "Z"*(8 - len(var)))

if (len(sys.argv) < 1):
    print("none")
else:
    for i in range (1,len(sys.argv)):
        if (len(sys.argv[i]) > 8):
            shrink(sys.argv[i])
        elif (len(sys.argv[i]) < 8):
            enlarge(sys.argv[i])
        else:
            print(sys.argv[i])