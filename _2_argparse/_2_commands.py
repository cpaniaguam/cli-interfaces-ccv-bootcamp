#!/usr/bin/env python3
"""
Compute statistics on a list of numbers
"""

import argparse
from funcs import mean, geom_mean, lp, kth

stat_functions = {
    "mean": mean,
    "geomean": geom_mean,
    "l2": lambda nums: lp(nums, 2),
    "1st": lambda nums: kth(nums, 2),
}


def main():
    description = __doc__
    epilog = "Example: python _2_commands.py l2 -n 1 2 3 4 5"

    parser = argparse.ArgumentParser(description=description, epilog=epilog)

    # Commands as positional arguments
    parser.add_argument(
        "stat", # name of the attribute in the args object
        choices=stat_functions.keys(),  # limit choices for the argument
        help="descriptor to compute",
    )

    # Data as keyword arguments
    parser.add_argument(
        "-n", # short option
        "--nums", # long option
        "--numbers", # alias for long option
        dest="nums", # name of attribute in args object
        type=float, # cast the argument to float
        nargs="+", # one or more arguments expected
        help="numbers to compute the descriptor on",
        required=True, # this *option* is required
    )

    args = parser.parse_args()

    # Get the function from the dictionary and call it
    f = stat_functions[args.stat]
    output = f(args.nums)
    print(output)


if __name__ == "__main__":
    main()

# Exercises
# 2. What happens if `nargs` is set to `1` instead of `"+"` or deleted?
# 3. Modify the program to accept a list of numbers from a data file
# 4. Add a new command to the CLI (e.g. mode, median, variance, standard deviation, etc.)
# 5. Make the stat command an option instead of a positional argument
