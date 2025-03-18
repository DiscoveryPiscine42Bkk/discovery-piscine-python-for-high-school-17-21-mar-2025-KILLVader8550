#!/usr/bin/env python3

import sys

if (len(sys.argv) > 1):
    def downcase_it (text):
        return text.lower()
    for i in sys.argv[1:]:
        print(downcase_it(i))

else:
    print("none")
