#!/usr/bin/env python3
from time import sleep


def main():
    print("hello from script")
    print("This script does some serious work")

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
