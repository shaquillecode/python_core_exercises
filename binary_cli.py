import argparse
from converter import *

parser = argparse.ArgumentParser(
                    description="Tool for converting numbers to binary and vice versa")
group = parser.add_mutually_exclusive_group() 
group.add_argument('-n2b', '--numtobin', action='store', help='takes a number and returns a string of that number in binary')
group.add_argument('-b2n', '--bintonum', action='store', help='takes a string of binary and returns the numbers it equates to')
parser.add_argument('--ascii', action='store', help='takes a string and returns the ascii for each character')
parser.add_argument('--ascii_sum', action='store', help='takes a string and returns a sum of the ascii numbers for all the characters')

args = parser.parse_args()

# print(args)

if args.numtobin:
    print(num_to_bin(args.numtobin))

if args.bintonum:
    print(bin_to_num(args.bintonum))

if args.ascii:
    print(list_ascii(args.ascii))

if args.ascii_sum:
    print(ascii_sum(args.ascii_sum))


