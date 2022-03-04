"""
Number to Binary converter
Binary to Number converter
String to ascii and ascii_sum converter
"""
import argparse
from format_converter import *

parser = argparse.ArgumentParser(description="Tool for converting numbers to binary and vice versa")
group = parser.add_mutually_exclusive_group()
group.add_argument('-nb', '--numtobin', action='store', help='Returns a string of binary')
group.add_argument('-bn', '--bintonum', action='store', help='Returns the number from a given binary string')
parser.add_argument('--ascii', action='store', help='Returns the ascii number for each character')
parser.add_argument('--ascii_sum', action='store', help='Returns a sum of the ascii numbers for all the characters from a given string')

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