import unittest
from core import Core

class EditDistanceTests(unittest.TestCase):
    
    @classmethod
    def setUp(cls):
        cls.solution = Core()


    def test_edit_distance(self):
        self.assertEqual(self.solution.edit_distance("the", "the"),0)
        self.assertEqual(self.solution.edit_distance("hen", "ben"),1)
        self.assertEqual(self.solution.edit_distance("the", "then"), 1)
        self.assertEqual(self.solution.edit_distance("then", "the"), 1)
        self.assertEqual(self.solution.edit_distance("the", "again"), 5)

if __name__ == '__main__':
    unittest.main()