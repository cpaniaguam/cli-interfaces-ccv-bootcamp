#!/usr/bin/env python3

import argparse
from funcs import *


def main():

    # Share the numbers argument between all subparsers
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument(
        "--nums",
        type=float,
        nargs="+",
        help="Numbers to calculate mean of",
        required=True,
    )

    parser = argparse.ArgumentParser(description="Compute statistics")

    # Commands with subparsers
    # Instantiate the subparsers object
    subparsers = parser.add_subparsers(title="commands", dest="command")

    statshelp = f'Calculate: {", ".join(stat_functions.keys())}'
    regular_stats_parser = subparsers.add_parser(
        "stat", help=statshelp, parents=[parent_parser]
    )

    regular_stats_parser.add_argument(
        "stat",
        choices=stat_functions.keys(),  # limit choices for the argument
        help="Metric to calculate",
    )

    # Subparser for the lp command
    lp_parser = subparsers.add_parser(
        "lp", help="Calculate the Lp norm", parents=[parent_parser]
    )
    lp_parser.add_argument(
        "-p", type=float, default=2, help="The p value for the Lp norm"
    )

    # Subparser for the nth command
    nth_parser = subparsers.add_parser(
        "nth", help="Calculate the nth ordered statistic", parents=[parent_parser]
    )
    nth_parser.add_argument(
        "-n", type=int, help="The n value for the nth ordered statistic"
    )

    args = parser.parse_args()

    if args.command == "lp":
        print(lp(args.nums, args.p))
    elif args.command == "nth":
        print(nth_ordered_stat(args.nums, args.n))
    else:
        # Get the function from the dictionary and call it
        print(stat_functions[args.stat](args.nums))


if __name__ == "__main__":
    main()

# Exercises
# 1. Inspect the help message for the CLI, and the help message for each command
# 2. Add a new command with argument to the CLI (e.g. topn, bottomn, etc.)
# 3. Modify the program to accept a list of numbers from a data file
# 4. Make the stat command an option instead of a positional argument
