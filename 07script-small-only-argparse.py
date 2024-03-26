import sys
import argparse
from time import sleep

script = __file__

# Set up the argument parser
parser = argparse.ArgumentParser(
    description="Do some serious work with data from a file."
)

parser.add_argument(
    "-b","--bound",
    metavar="N",
    type=int,
    dest="bound",
    default=2,
    help="upper bound for work time",
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
with open("inputdata.dat", "r") as file:
    data = [int(line.rstrip("\n")) for line in file]

print(f"Hello from {script}")
print("We are going to do a lot of work now...")

for t in data:
    # Small jobs only please
    if t < args.bound:
        print(f"Doing some work for {t} seconds...")
        sleep(t)

print("Work done!")
