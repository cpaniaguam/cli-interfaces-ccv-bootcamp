#!/usr/bin/env python3
"""
Do some serious work with data from a file
"""
import argparse
from time import sleep

def do_work(t):
    sleep(t)


def main():

    # Set up the argument parser
    parser = argparse.ArgumentParser(
        description=__doc__,
        prog="dowork",
    )

    parser.add_argument(
        "-b",
        "--bound",
        metavar="N",  # metavar is (a more intuitive and friendlier) name of the argument in the help message
        type=int,  # type specifies to what type the argument should be converted
        dest="bound",  # dest is the name of the attribute in the args object
        default=2,  # default is the value the argument will have if not provided
        help="upper bound for work time",  # help is the help message for the argument
    )

    parser.add_argument(
        "-f",
        "--file",
        metavar="path",
        dest="datafile",
        default="inputdata.dat",
        help="the path to the data file",
    )

    # Parse the command line arguments
    args = parser.parse_args()

    # Do work with the parsed arguments
    with open(args.datafile, "r") as file:
        data = [int(line.rstrip("\n")) for line in file]

    print(f"Hello from {__name__}")
    print("We are going to do a lot of work now...")

    for t in data:
        # Small jobs only please
        if t < args.bound:
            print(f"Doing some work for {t} seconds...")
            do_work(t)

    print("Work done!")


if __name__ == "__main__":
    main()


# Exercise:
# 1. Run the script with the following command:
#    python 02argparse/00script-small-only-argparse.py
#    python 02argparse/00script-small-only-argparse.py --help
#    python 02argparse/00script-small-only-argparse.py -h

# 2. Run the script with the following command:
#    python 02argparse/00script-small-only-argparse.py -b 1
#    python 02argparse/00script-small-only-argparse.py -f inputdata.dat
#    python 02argparse/00script-small-only-argparse.py -b 1 -f otherinputdata.dat
#    python 02argparse/00script-small-only-argparse.py -b foo
