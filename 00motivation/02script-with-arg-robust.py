#!/usr/bin/env python3
from time import sleep


def main():
    print("Hello from script")
    print("This script does some serious work")
    t = input("How much work are we doing? ")

    try:
        amount_of_work = int(t)
    except ValueError:
        print("Invalid input. Aborting.")
        exit(1)

    print("Doing some work...")
    for _ in range(amount_of_work):
        sleep(0.5)
        print(".", end="", flush=True)
    print("\nWork done!")


if __name__ == "__main__":
    main()
