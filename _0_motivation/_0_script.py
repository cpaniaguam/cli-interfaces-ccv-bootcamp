#!/usr/bin/env python3
# _0_motivation/_0_script.py
"""
This script does some serious work
"""

# Entry point of the script at the top of the file
from time import sleep

print("Hello from", __name__) # look at this line for a moment. What's peculiar about it?
print(__doc__) # How about this one?

t = input("How much work are we doing? ")
amount_of_work = int(t)

print("Doing some work...")

for _ in range(amount_of_work):
    sleep(0.5)
    print(".", end="", flush=True)
print("\nWork done!")
