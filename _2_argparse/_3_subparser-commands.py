#!/usr/bin/env python3
"""
Compute statistics on a list of numbers
"""

import argparse
from funcs import mean, lp, kth

stat_functions = {f.__name__: f for f in [mean, lp, kth]}

def main():

    # Share the numbers argument between all subparsers
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument(
        "--nums",
        type=float,
        nargs="+",
        help="numbers to compute mean of",
        required=True,
    )

    description = __doc__
    epilog = "Example: python _3_subparser-commands.py lp -p 2 -n 1 2 3 4 5"
    parser = argparse.ArgumentParser(description=description, epilog=epilog)

    # Commands with subparsers
    # Instantiate the subparsers object
    subparsers = parser.add_subparsers(title="commands", dest="command", required=True)

    # Subparser for the mean command
    # param_free_parser =
    subparsers.add_parser(
        "mean",
        description=mean.__doc__,  # shown in the main help message
        help=mean.__doc__,  # shown in the help message for the command
        parents=[parent_parser],
    )

    # Subparser for the kth command
    kth_parser = subparsers.add_parser(
        "kth",
        description=kth.__doc__,  # shown in the main help message
        help=kth.__doc__,  # shown in the help message for the command
        parents=[parent_parser],
        epilog="Example: python _3_subparser-commands.py kth -k 3 --nums 1 2 3 4 5"
    )
    kth_parser.add_argument("-k", type=int, default=2, help="value for the kth order statistic", required=True)

    # Subparser for the lp command
    lp_parser = subparsers.add_parser(
        "lp", description=lp.__doc__, help=lp.__doc__, parents=[parent_parser]
    )
    lp_parser.add_argument(
        "-p", type=float, default=2, help="The p value for the lp norm"
    )

    args = parser.parse_args()


    f = stat_functions[args.command]

    if args.command == "lp":
        print(lp(args.nums, args.p))
    elif args.command == "kth":
        print(kth(args.nums, args.k))
    else: # parameter free functions
        print(f(args.nums))


if __name__ == "__main__":
    main()

# Exercises
# 1. Inspect the help message for the CLI, and the help message for each command
# 2. Add a new command with argument to the CLI (e.g. topn, bottomn, etc.)
# 3. Modify the program to accept a list of numbers from a data file
# 4. Make the stat command an option instead of a positional argument
