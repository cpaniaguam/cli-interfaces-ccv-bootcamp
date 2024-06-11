#!/usr/bin/env python3
"""
This script does some serious work
"""

from time import sleep

def main():
    print("Hello from", __name__) # look at this line for a moment. What's peculiar about it?
    print(__doc__) # How about this one?

    t = input("How much work are we doing? ")
    amount_of_work = int(t)

    print("Doing some work...")

    for _ in range(amount_of_work):
        sleep(0.5)
        print(".", end="", flush=True)
    print("\nWork done!")


if __name__ == "__main__":
    # This is the entry point of the script
    main()
