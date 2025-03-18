#!/usr/bin/env python3

import sys

if (len(sys.argv)-1 == 2):
    if (sys.argv[2].split().count(sys.argv[1])) == 0:
        print("none")
    else:
        print(sys.argv[2].split().count(sys.argv[1]))
else:
    print("none")