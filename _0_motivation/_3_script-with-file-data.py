#!/usr/bin/env python3
from time import sleep


def main():
    # use a data file
    with open("inputdata.dat", "r") as file:
        data = [int(line.rstrip("\n")) for line in file]

    print("We are going to do a lot of work now...")
    for t in data:
        print(f"\n\tDoing {t} units of work...")
        print("\t", end="", flush=True)
        for _ in range(t):
            sleep(0.5)
            print(".", end="", flush=True)
        print("\n\tWork done!")


if __name__ == "__main__":
    main()
