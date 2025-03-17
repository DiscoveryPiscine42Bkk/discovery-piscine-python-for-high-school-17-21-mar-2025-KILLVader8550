#!/usr/bin/env python3

import sys

if (len(sys.argv) > 1):
    for i in sys.argv:
        print(i.lower())
else:
    print("none")
