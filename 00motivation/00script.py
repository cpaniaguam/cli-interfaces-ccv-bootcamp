#!/usr/bin/env python3

# Entry point of the script at the top of the file
from time import sleep

print("Hello from script")
print("This script does some serious work")

t = input("How much work are we doing? ")
amount_of_work = int(t)

print("Doing some work...")

for _ in range(amount_of_work):
    sleep(0.5)
    print(".", end="", flush=True)
print("\nWork done!")
