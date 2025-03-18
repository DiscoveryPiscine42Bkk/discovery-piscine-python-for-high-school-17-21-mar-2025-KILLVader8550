#!/usr/bin/env python3

import sys

parameter = sys.argv[1:]
result = []

if (len(parameter) == 2):
    for i in range (int(parameter[-1]) - int(parameter[0]) + 1):
        result.append(int(parameter[0]) + i)
    print(result)
else:
    print("none")
