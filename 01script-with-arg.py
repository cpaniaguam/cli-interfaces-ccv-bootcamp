#!/usr/bin/env python3
from time import sleep

def main():
    print('hello from script')
    print('This script does some serious work')

    t = input('How much work are we doing? ')

    print('Doing some work...')
    sleep(int(t))

    print('Work done!')

if __name__ == '__main__':
    main()