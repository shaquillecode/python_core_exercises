import unittest
from core.py import core

Class CoreAddTests(unittest.TestCase):

def test_count_alphabet(test_input):
    """ 
    Test the ability to count only the alphabet from a given sequence of string"
	"""
    test_input.assertEqual(countAll("P@#yn26at^&i5ve"), )
    pass

def test_count_digits():
    """ 
    Test the ability to count only the digits 0 - 9 from a given sequence of string"
	"""
    pass

def test_count_special():
    """ 
    Test the ability to count all the special characters which is not digits 0 - 9 or the alphabet from a given sequence of string"
	"""
    pass

# class CalculatorAddTests(unittest.TestCase):

# 	@classmethod
# 	def setUpClass(cls):
# 		"""
# 		instantiate our class  (fixture)
# 		"""
# 		cls.calc = Calculator()

# 	def test_add_integers(self):
# 		""" 
# 		Test the addition of integers
# 		"""
# 		self.assertEqual(self.calc.add(2,3), 5)

# 	def test_add_floats(self):
# 		""" 
# 		Test the addition of floats
# 		"""
# 		self.assertEqual(self.calc.add(2.0,3.2), 5.2)

if __name__ == '__main__':
    unittest.main()