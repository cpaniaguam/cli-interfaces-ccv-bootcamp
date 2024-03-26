from time import sleep

def main():
    with open('inputdata.dat', 'r') as file:
        data = [int(line.rstrip('\n')) for line in file]

    print('We are going to do a lot of work now...')
    for t in data:
        print(f'Doing some work for {t} seconds...')
        sleep(t)
    print('Work done!')

if __name__ == '__main__':
    main()