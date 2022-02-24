"""
Returns the sum of following series upto nth term(parameter)
Input  = 6
Output = sum(1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16)
"""
import unittest
from core import Core


class AddSeriesTest(unittest.TestCase):
    """
    Test for finding the sum of the following series upto nth term(parameter)
    """
    @classmethod
    def setUp(cls):
        """
        Instantiating class/object
        """
        cls.solution = Core()

    def test_add_series(self):
        """
        Returns the sum of following series upto nth term(parameter)
        Returns a string result or 0.0
        """
        self.assertEqual(self.solution.add_series(0), 0.0)
        self.assertEqual(self.solution.add_series(1),"1.0")
        self.assertEqual(self.solution.add_series(2), "1.25")
        self.assertEqual(self.solution.add_series(5), "1.57")

if __name__ == '__main__':
    unittest.main()