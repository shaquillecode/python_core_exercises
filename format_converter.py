"""
Format converter
"""
# Ex. A
# python3 format_converter_cli.py --ascii_sum "hello world"
# -> 1116
def ascii_sum(str_):
    """
    Returns a sum of the ascii numbers 
    for all the characters from a given string
    """
    sum_of_letts = sum([ord(x) for x in str_])
    return sum_of_letts


# Ex. B
# python3 format_converter_cli.py --ascii "hello world"
# [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]
def list_ascii(str_):
    """
    Returns the ascii number
    for each character from a given string
    """
    nums = [ord(x) for x in str_]
    return nums

# Ex. C
# python3 format_converter_cli.py  -nb 45
def num_to_bin(num):
    """
    Returns a string of binary
    from a given integer
    """
    num = int(num)
    res = str(bin(num))[2:]
    return res

# Ex. D
# python3 format_converter_cli.py -bn "101101"
def bin_to_num(bin):
    """
    Returns a integer 
    from a given binary string
    """
    return int(bin, 2)