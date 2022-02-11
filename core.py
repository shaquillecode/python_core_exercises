"""
A module for core python programming practice
"""

class Core:
    """
    A module for core python programming practice
    """

    def even_words_only(self,phrase):
        """
        This will print all the words with an even length in the given string
        """
        return " ".join([even for even in phrase.split() if len(even) % 2 == 0 ])


    def add_it_up(self,num):
        """
        Returns sum of the integers from zero to the given integer
        Return 0 if a non-integer is passed in
        """
        if isinstance(num, int):
            return sum([i for i in range(1,num+1)])
        else:
            return 0


    def count_alphabet(self,str1):
        """
        Counts all of the Alphabetic characters from a given sequence of string
        """

        alphabet = ""
        for i,char in enumerate(str1):
            if((str1[i] >= 'A' and str1[i] <= 'Z') or (str1[i] >= 'a' and str1[i] <= 'z')):
                alphabet += str1[i]
        # print(alphabet)
        # print(f"This is the count for all of the Alphabetic characters {len(alphabet)}")
        return len(alphabet)


    def count_digit(self,str1):
        """
        Counts only the digits 0 - 9 from a given sequence of string
        """

        digits = ""
        for i,char in enumerate(str1):
            if str1[i].isdigit():
                digits = digits + str1[i]
        # print(digits)
        # print(f"This is the count for Digits {len(digits)}")
        return len(digits)


    def count_symbol(self,str1):
        """
        Counts only special symbols from a given sequence of string
        """
        alphabet = ""
        digits = ""
        symbols = ""
        for i,char in enumerate(str1):
            if str1[i].isdigit():
                digits = digits + str1[i]
            elif((str1[i] >= 'A' and str1[i] <= 'Z') or (str1[i] >= 'a' and str1[i] <= 'z')):
                alphabet += str1[i]
            else:
                symbols += str1[i]
        # print(symbols)
        # print(f"This is the count for Symbols {len(symbols)}")
        return len(symbols)


    def edit_distance(self,str1, str2):
        """
        case 1: the same length
        case 2: they are not the same length
        """

        # if the strings are the same, edit distance = 0
        if str1 == str2:
            return 0

        # if the strings are the same length
        # ben, hen
        if len(str1) == len(str2):
            counter = 0
            for idx, ch_ in enumerate(str1):
                if ch_ != str2[idx]:
                    counter += 1

            return counter

        if len(str1) != len(str2):
            counter = 0
            # add the difference
            # i.e. the then -> 4 - 3 =  1

            larger = None
            smaller = None

            if len(str1) > len(str2):
                larger = str1
                smaller = str2
            else:
                larger = str2
                smaller = str1

            offset = len(larger) - len(smaller)
            counter += offset

            for idx, ch_ in enumerate(smaller):
                if ch_ != larger[idx]:
                    counter += 1

            return counter


    def is_anagram(self,char1,char2):
        """
        Checks if two strings (char1 and char2) are anagrams of each other
        """
        if isinstance(char1,str) and isinstance(char2,str):
            # print(sorted(char1))
            # print(sorted(char2))

            if sorted(char1) == sorted(char2):
                return True
        return False






if __name__ == '__main__':
    STR_J = "P@#yn26at^&i5ve"
    WD_1 = "the"
    WD_2 = "again"
    INTRO = "My name is Shaquille"
    solution = Core()
    print(solution.even_words_only(INTRO))
    print(solution.add_it_up(10))
    print(
        f"The distance of '{WD_1}' and '{WD_2}' is { solution.edit_distance(WD_1, WD_2)}")
    print(solution.count_alphabet(STR_J))
    print(solution.count_digit(STR_J))
    print(solution.count_symbol(STR_J))
    print(solution.is_anagram("state","taste"))