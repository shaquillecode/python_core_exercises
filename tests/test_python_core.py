"""
Test class for core python programming practice
"""
import unittest
from core import Core
from caesar_cipher import ceasar_cipher

class CorePythonTest(unittest.TestCase):
    """
    Test class for core python programming practice
    """
    @classmethod
    def setUp(cls):
        """
        Instantiating class/object
        """
        cls.solution = Core()

    def test_count_alpha(self):
        """
        Test for counting all of the Alphabetic characters from a given sequence of string
        """

        str1 = "P@#yn26at^&i5ve"
        self.assertEqual(self.solution.count_alphabet(str1), 8)

    def test_count_digit(self):
        """
        Test for counting only the digits 0 - 9 from a given sequence of string
        """

        str1 = "P@#yn26at^&i5ve"
        self.assertEqual(self.solution.count_digit(str1), 3)

    def test_count_symbol(self):
        """
        Test for counting only special symbols from a given sequence of string
        """
        str1 = "P@#yn26at^&i5ve"
        self.assertEqual(self.solution.count_symbol(str1), 4)

    def test_even_words_only(self):
        """
        Test to print all words with even length in the given string
        """
        phrase = "This is a python language"
        result = "This is python language"
        self.assertEqual(self.solution.even_words_only(phrase), result)

    def test_add_it_up(self):
        """
        Test to return sum of the integers from zero to the given integer
        Return 0 if non-integer
        """
        self.assertEqual(self.solution.add_it_up(5), 15)
        self.assertEqual(self.solution.add_it_up(5.2), 0)

    def test_caesar_cipher(self):
        """
        Caesar Cipher
        """
        plane_text = "abcd xyzzzz ZZZZ"
        cipher_text = "EFGH BCDDDD DDDD"
        self.assertEqual(ceasar_cipher(plane_text,4), cipher_text)


if __name__ == '__main__':
    unittest.main()