"""
A module for core recursion python programming practice
"""
from itertools import permutations

class CoreRecursive:
    """
    A module for core recursion python programming practice
    """

    def countdown(self, num):
        """
        This recursion function will count down
        output will be in reverse order 0,1,2,3,4,5
        """

        # countdown(5) -
	    # -> countdown(4) - print(4) resolved
 		#     -> countdown(3)- print(3) resolved
 		# 	    -> countdown(2) - print(2) resolved
 		# 		    ->  countdown(1) - print(1) resolved
 		# 			    -> -> countdown(0) -> print(0) -resolved
        if num != 0:
            self.countdown(num-1)
        print(num, end = " ",)

    def all_divs(self, num):
        """
        This will print all the numbers divisble by 2 up until that number
        """
        if num == 1:
            return
        if num % 2 == 0:
            print(num, end = " ")
        return self.all_divs(num - 1)


    def build_str(self, a_str, n=3):
        """
        This is a recursive function that takes a string of two letters
        and returns the following: 'ab', 'aabb', 'aaabbb'
        """
    # build_str(3) = ab + build_str(2)
    # build_str(2) = ab + build_str(1)
    # build_str(1) = ab

    # ->
    # build_str(2) = ab + ab = abab
    # build_str(3) = ab + abab
    # build_str(3) = ababab

        if n == 0:
            return

        if n == 1:
            return a_str

        return a_str[0] + self.build_str(a_str, n - 1) + a_str[1]

    def insert_letter(self, word, letter):
        """
        Recursion insert letter function
        """
        # insert_letter('the', 'a') =  't' + 'a' + insert_letter('he', 'a')
        # insert_letter('he', 'a') = 'h' + 'a' + insert_letter('e', 'a')
        # insert_letter('e', 'a') =  'e' + 'a' + insert_letter('', 'a')
        # insert_letter('','a') =  ''
        # -> tahaea
        if len(word) == 0:
            return ''

        return word[0] + letter + self.insert_letter(word[1:], letter)

    def print_pascal(self, num):
        """
        Print out pascal's triangle
        simplest case / base case: n= 1 -> [1]
        n = 2
        """

        if num == 1:
            return [1]
        else:

            # row in pyramid always starts with 1
            line = [1]

            # recursive call to print_pascal (look at previous line)
            prev_line = self.print_pascal(num - 1)

            # add elements based on sum of previous line
            for i in range(len(prev_line) - 1):
                line.append(prev_line[i] + prev_line[i+1])

            # row in pyramid always ends with 1
            line += [1]

        return line

    def power_func(self, a, b):
        """
        This will calculate the value of 'a' to the power 'b'
        """
        # base cases
        if b == 0:
            return 1
        elif b == 1:
            return a
        else:
            return a * self.power_func(b-1)


    def factorial_(self, num):
        """
        This will calculate the factorial
        """
        # 1! = 1, 0! = 1
        if num == 0 or num == 1:
            return 1
        elif num > 1:
            return num * self.factorial_(num-1)


    def rev_list(self, MyList = [37, 1, 26]):
        """
        This will reverse a list
        """
        if len(MyList) == 0:
            return []
        else:
            return [MyList.pop()] + self.rev_list(MyList)

    def find_digit_combo(self, str_num, spacer, combos, curr=""):
        """ Finds digits combo"""

        if not str_num and not spacer:
            res = " ".join(curr.split())
            combos.add(res)

        if str_num:
            self.find_digit_combo(str_num[1:], spacer, combos, curr+str_num[0])
        if spacer:
            self.find_digit_combo(str_num, spacer[1:], combos, curr+spacer[0])

        return combos

    def digit_combo(self, num):
        """Digit combo"""
        str_num = str(num)
        spacer = " "*len(str_num)
        combos = set()

        if not str_num:
            return combos

        return self.find_digit_combo(str_num, spacer, combos)


    def findInterleavings(self, X, Y, interleavings, curr=''):
        """
        Recursive Function to find all interleaving of string `X` and `Y`
        """
        # insert `curr` into the set if the end of both strings is reached
        if not X and not Y:
            interleavings.add(curr)
            return

        # if the string `X` is not empty, append its first character in the
        # result and recur for the remaining substring

        if X:
            self.findInterleavings(X[1:], Y, interleavings, curr + X[0])

        # if the string `Y` is not empty, append its first character in the
        # result and recur for the remaining substring

        if Y:
            self.findInterleavings(X, Y[1:], interleavings, curr + Y[0])

        return interleavings


    def findAllInterleavings(self, X, Y):
        """Finds All Interleavings"""

        # use set to handle duplicates
        interleavings = set()

        if not X and not Y:
            return interleavings

        self.findInterleavings(X, Y, interleavings)
        return interleavings


    def divThreeFive(self, myList = [3, 6, 9, 15, 30, 45], res = []):
        """
        Takes a list of numbers and prints all the numbers divisble by 3 and 5
        """
        if len(myList) == 0:
            return []

        if myList[0]% 3 == 0 and myList[0] % 5 == 0:
            res.append(myList[0])

        self.divThreeFive(myList[1:])
        return res

    def isPalindrome(self,str1):
        """
        Recursion function to check if a string is a palindrome
        """
        # "RACECAR", "ACECA", "CEC", "E", ""=> This will return True at base case then will go backwards
        if isinstance(str1,str):
            if len(str1) == 0:
                return True
            else:
                if str1[0] == str1[-1]:
                    return self.isPalindrome(str1[1:-1])
                return False


    def printLexicographicOrder(self, str1, result=''):
        """Print Lexicographic"""

        if len(result) == len(str1):
            print(result, end=' ')
            return

        for c in str1:
            self.printLexicographicOrder(str1, result + c)


    def findLexicographic(self, str1):
        """ Find Lexicographic """

        if not str1:
            return

        c = sorted(list(str1))

        self.printLexicographicOrder(c)


    def perm(self, str1):
        """Find Permutations of abc"""
        # 'a', 'b', 'c'
        # 'a', 'c', 'b'
        # 'b', 'a', 'c'
        # 'b', 'c', 'a'
        # 'c', 'a', 'b'
        # 'c', 'b', 'a'
        # 6 total permutations for abc
        return ["".join(letters) for letters in permutations(str1)]

    def encode(self, str_, mappings = {'X':'code', 'Y': 'sleep'}):
        """
        Given a string and a pattern, determine whether a string matches with a given pattern.
        """

        res = ''

        # look at every character position
        for char_index in range(len(str_)):

            # try matching each mapping from given char_index
            for key,val in mappings.items():
                end_index = len(val) + char_index

                if val == str_[char_index: end_index]:
                    res += key
                    break

        return res

if __name__ == '__main__':
    solution = CoreRecursive()
    X = 'ABC'
    Y = 'ACB'

    solution.countdown(5)
    print()
    solution.all_divs(10)
    print()
    print(solution.build_str('ab', 3))
    print(solution.insert_letter('the', 'a'))
    print("==="*35)

    print(solution.print_pascal(1))
    print(solution.print_pascal(2))
    print(solution.print_pascal(3))
    print(solution.print_pascal(4))
    print("==="*35)

    # solution.power_func(2, 4)
    print("==="*35)

    print(solution.factorial_(5))
    print("==="*35)

    print(solution.rev_list())
    print(solution.rev_list([3,2,1]))
    print("==="*35)

    print(solution.digit_combo(123))
    print(solution.digit_combo(1234))
    print("==="*35)

    interleavings = solution.findAllInterleavings(X, Y)
    print(interleavings)
    print("==="*35)

    print(solution.divThreeFive())
    print("==="*35)

    print(solution.isPalindrome("RACECAR"))
    print(solution.isPalindrome("DOOR"))
    print("==="*35)

    solution.findLexicographic('ACB')
    print("==="*35)

    print(solution.perm('abc'))
    print([letters for letters in permutations('abc')])
    print("==="*35)

    print(solution.encode("codesleepcode"))
    print(solution.encode("ccodestufff"))
    print("==="*35)
