# Exercise 1
# Count all letters, digits, and special symbols from a given string

# input: str1 = "P@#yn26at^&i5ve"

# output: Total counts of chars, digits, and symbols 

# Chars = 8 
# Digits = 3 
# Symbol = 4

class Core:

    """ 
    A module for multiple in class python core assignments  
    """

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

if __name__ == '__main__':
    str1 = "P@#yn26at^&i5ve"
    solution = Core()
    print(solution.countAlphabet(str1))
    print(solution.countDigit(str1))
    print(solution.countSymbol(str1))