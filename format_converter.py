"""
Format converter
"""
# Ex A
# python3 binary_cli.py --ascii_sum "hello world"
# -> 1116
def ascii_sum(str_):
    """
    Sum of ascii numbers
    Format converter
    """
    sum_of_letts = sum([ord(x) for x in str_])
    return sum_of_letts


# Ex. B
# python3 binary_cli.py --ascii "hello world"
# [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]
def list_ascii(str_):
    """
    List of ascii numbers
    Format converter
    """
    nums = [ord(x) for x in str_]
    return nums

# Ex. C
# python3 binary_cli.py -bn "101101"
def num_to_bin(num):
    """
    Number to Binary
    Format converter
    """
    num = int(num)
    res = str(bin(num))[2:]
    return res

# Ex. D
# python3 binary_cli.py -nb 45
def bin_to_num(bin):
    """
    Binary to Number
    Format converter
    """
    return int(bin, 2)