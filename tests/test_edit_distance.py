"""
This class finds minimum number of edits (operations)
"""
import unittest
import csv
from core import Core

class EditDistanceTest(unittest.TestCase):
    """
    This class finds minimum number of edits (operations)
    """
    @classmethod
    def setUp(cls):
        """
        Instantiating class/object
        """
        cls.solution = Core()


    def test_edit_distance(self):
        """
        Test for finding minimum number of edits (operations) required to convert str1 into str2
        """
        self.assertEqual(self.solution.edit_distance("the", "the"),0)
        self.assertEqual(self.solution.edit_distance("hen", "ben"),1)
        self.assertEqual(self.solution.edit_distance("the", "then"), 1)
        self.assertEqual(self.solution.edit_distance("then", "the"), 1)
        self.assertEqual(self.solution.edit_distance("the", "again"), 5)

    def test_edit_distance_bulk(self):
        """
        randomly generated examples for edit distance
        """
        with open('data/wordlist.csv') as csvfile:
            examples = csv.reader(csvfile)
            for row in examples:
                self.assertEqual(self.solution.edit_distance(row[0], row[1]), int(row[2]))

if __name__ == '__main__':
    unittest.main()