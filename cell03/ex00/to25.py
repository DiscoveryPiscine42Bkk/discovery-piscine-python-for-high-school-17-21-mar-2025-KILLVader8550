#!/usr/bin/env python3
import time

num = int(input("Enter a number less than 25\n"))

if (num <= 25): 
    while (num <= 25):
        print(f"Inside the loop, my variable is {num}")
        num += 1
        time.sleep(1)
else:
    print("Error")
