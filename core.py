class Core:

    """ 
    A module for multiple in class python core assignments  
    """
    def edit_distance(self,str1, str2):
        """
        case 1: the same length 
        case 2: they are not the same length 
        """

        # if the strings are the same, edit distance = 0
        if str1 == str2:
            return 0

        # the case if the strings are the same length
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
    
    def countAlphabet(self,str1):
        """
        This is the count for all of the Alphabetic characters from a given sequence of string
        """
    
        Alphabet = ""
        for i in range(len(str1)):
            if((str1[i] >= 'A' and str1[i] <= 'Z') or (str1[i] >= 'a' and str1[i] <= 'z')):
                Alphabet += str1[i]

        # print(Alphabet)
        # print(f"This is the count for all of the Alphabetic characters {len(Alphabet)}") 
        return len(Alphabet)


    def countDigit(self,str1):
        """
        This is the count for only the digits 0 - 9 from a given sequence of string
        """

        Digits = ""
        for i in range(len(str1)):
            if (str1[i].isdigit()):
                Digits = Digits + str1[i]

        
        # print(Digits)
        # print(f"This is the count for Digits {len(Digits)}")
        return len(Digits)

    def countSymbol(self,str1):
        """
        This is the count for only special symbols and not alphanumeric characters from a given sequence of string
        """
    
        Alphabet = ""
        Digits = ""
        Symbols = ""
        for i in range(len(str1)):
            if (str1[i].isdigit()):
                Digits = Digits + str1[i]
            elif((str1[i] >= 'A' and str1[i] <= 'Z') or (str1[i] >= 'a' and str1[i] <= 'z')):
                Alphabet += str1[i]
            else:
                Symbols += str1[i]

        # print(Symbols)
        # print(f"This is the count for Symbols {len(Symbols)}")
        return len(Symbols)

    def is_anagram(self,char1,char2):
        """
        This will check if the given sequence of the two strings (char1 and char2) are anagrams of each other
        """
        if isinstance(char1,str) and isinstance(char2,str):
            # print(sorted(list(char1)))
            # print(sorted(list(char2)))

            if sorted(char1) == sorted(char2):
                return True
        return False


if __name__ == '__main__':
    str1 = "P@#yn26at^&i5ve"
    WD_1 = "the"
    WD_2 = "hen"
    WD_3 = "ben"
    WD_4 = "then"
    WD_5 = "again"
    solution = Core()
    print(
        f"The distance of '{WD_1}' and '{WD_1}' is { solution.edit_distance(WD_1, WD_1)}")
    print(
        f"The distance of '{WD_2}' and '{WD_3}' is { solution.edit_distance(WD_2, WD_3)}")
    print(
        f"The distance of '{WD_1}' and '{WD_4}' is { solution.edit_distance(WD_1, WD_4)}")
    print(
        f"The distance of '{WD_1}' and '{WD_4}' is { solution.edit_distance(WD_4, WD_1)}")
    print(
        f"The distance of '{WD_1}' and '{WD_5}' is { solution.edit_distance(WD_1, WD_5)}")
    print(solution.countAlphabet(str1))
    print(solution.countDigit(str1))
    print(solution.countSymbol(str1))
    print(solution.is_anagram("state","taste"))
    print(solution.is_anagram(9.2,"taste"))