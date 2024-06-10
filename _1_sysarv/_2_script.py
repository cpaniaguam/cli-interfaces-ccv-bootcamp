#!/usr/bin/env python3
"""
This script does some serious work
"""

import sys
from time import sleep

def do_work(t):
    sleep(t)

def main():
    # ISSUE: args are positional, need prior knowledge of the script for correct use
    script, bound, filepath = sys.argv # ISSUE: What if there are not enough or extra arguments?
    print(__doc__)
    print(f'{script=}, {bound=}, {filepath=}')


    # Read the data from file
    with open(filepath, 'r') as file:
        data = [int(line.rstrip('\n')) for line in file]

    print(f'Hello from {script}')
    print('We are going to do a lot of work now...')

    for t in data:
        # Small jobs only please
        if t < int(bound): # ISSUE: What if bound cannot be cast to int?
            print(f'Doing some work for {t} seconds...')
            do_work(t)

    print('Work done!')


if __name__ == '__main__':
    main() # this is the code's entry point when the script is run from the command line