import unittest
from core import Core

class CountStringTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.solution = Core()

    def test_count_alpha(self):
        """
        This is a Test for counting all of the Alphabetic characters from a given sequence of string
        """

        str1 = "P@#yn26at^&i5ve" 
        self.assertEqual(self.solution.countAlphabet(str1), 8)

    def test_count_digit(self):
        """
        This is a Test for counting only the digits 0 - 9 from a given sequence of string
        """

        str1 = "P@#yn26at^&i5ve" 
        self.assertEqual(self.solution.countDigit(str1), 3)

    def test_count_symbol(self):
        """
        This is a Test for counting only special symbols and not alphanumeric characters from a given sequence of string
        """
        str1 = "P@#yn26at^&i5ve" 
        self.assertEqual(self.solution.countSymbol(str1), 4)



if __name__ == '__main__':
    unittest.main()