import unittest
from core import Core

class AnagramTests(unittest.TestCase):
    
    @classmethod
    def setUp(cls):
        cls.solution = Core()


    def test_is_anagram(self):
        """
        This is a test that will check if the given sequence of the two strings (char1 and char2) are anagrams of each other
        """
        self.assertEqual(self.solution.is_anagram("arc","car"),True)
        self.assertEqual(self.solution.is_anagram("brag","grab"),True)
        self.assertEqual(self.solution.is_anagram("state","taste"), True)
        self.assertEqual(self.solution.is_anagram("everybody","jump"), False)
        self.assertEqual(self.solution.is_anagram(True,"not"), False)
        self.assertEqual(self.solution.is_anagram(9.3,"nifty"), False)

if __name__ == '__main__':
    unittest.main()