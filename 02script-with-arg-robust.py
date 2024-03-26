from time import sleep

def main():
    print('hello from script')
    print('This script does some serious work')
    t = input('How much work are we doing? ')
    print('Doing some work...')

    try:
        sleep(int(t))
    except ValueError:
        print('Invalid input. Aborting.')
        exit(1)
    print('Work done!')

if __name__ == '__main__':
    main()