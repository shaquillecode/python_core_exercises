# Exercise 4

# Ex A
# python3 format_converter.py 'hello world' --ascii_sum 
# -> 1116
def ascii_sum(str_):
    sum_of_letts = sum([ord(x) for x in str_])
    return sum_of_letts

ascii_sum('hello world')

# Ex. B
# python3 format-converter.py 'hello world' --ascii 
# -> [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]
def list_ascii(str_):
    nums = [ord(x) for x in str_]
    return nums

list_ascii('hello world')


# Ex. C
# python3 format-converter.py 45 --bin
# -> 101101
def num_to_bin(num):
    num = int(num)
    res = str(bin(num))[2:]
    return res

def bin_to_num(bin):
    return int(bin, 2)