"""
Returns a sum of the ascii numbers for all the characters from a given string
Returns the ascii number for each character from a given string
Returns a string of binary from a given integer
Returns a integer from a given binary string
"""
import argparse
from format_converter import *

parser = argparse.ArgumentParser(description="Tool for converting numbers to binary and vice versa")
group = parser.add_mutually_exclusive_group()
parser.add_argument('--ascii_sum', action='store', help='Returns a sum of the ascii numbers')
parser.add_argument('--ascii', action='store', help='Returns the ascii number')
group.add_argument('-nb', '--numtobin', action='store', help='Returns a string of binary')
group.add_argument('-bn', '--bintonum', action='store', help='Returns a integer')

args = parser.parse_args()
# print(args)

if args.ascii_sum:
    print(ascii_sum(args.ascii_sum))

if args.ascii:
    print(list_ascii(args.ascii))

if args.numtobin:
    print(num_to_bin(args.numtobin))

if args.bintonum:
    print(bin_to_num(args.bintonum))