#!/usr/bin/env python3

import argparse
from funcs import *


def main():

    parser = argparse.ArgumentParser(description="Compute statistics")

    stat_functions["l2"] = lambda nums: lp(nums, 2)

    # Commands
    parser.add_argument(
        "stat",
        choices=stat_functions.keys(),  # limit choices for the argument
        help="Metric to calculate",
    )

    # Data
    parser.add_argument(
        "--nums",
        "--numbers",
        type=float,
        nargs="+",
        help="Numbers to calculate mean of",
        required=True,
    )

    args = parser.parse_args()

    # Get the function from the dictionary and call it
    print(stat_functions[args.stat](args.nums))


if __name__ == "__main__":
    main()

# Exercises
# 1. Add a new command to the CLI (e.g. mode, median, variance, standard deviation, etc.)
# 2. Modify the program to accept a list of numbers from a data file
# 3. Make the stat command an option instead of a positional argument
