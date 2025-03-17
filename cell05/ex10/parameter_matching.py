#!/usr/bin/env python3

import sys

user_input = input("What was the parameter? ")

if (sys.argv[1] == user_input):
    print("Good Job!")
else:
    print("Nope, sorry...")