import sys
from time import sleep

def main():
    # args are positional, need prior knowledge of the script
    script, bound, filepath = sys.argv[0], sys.argv[1], sys.argv[2]

    with open(filepath, 'r') as file:
        data = [int(line.rstrip('\n')) for line in file]

    print(f'Hello from {script}')
    print('We are going to do a lot of work now...')

    for t in data:
        # Small jobs only please
        if t < int(bound):
            print(f'Doing some work for {t} seconds...')
            sleep(t)

    print('Work done!')


if __name__ == '__main__':
    main()
    