import unittest
from BinarySearch import BinarySearch

class BinarySearchTest(unittest.TestCase):
    def test_binary_one(self):
        self.assertEqual(BinarySearch().search([1, 2, 3, 4], 3), 2)
    def test_binary_two(self):
        self.assertEqual(BinarySearch().search([2, 3, 5, 8], 2), 0)
    def test_binary_three(self):
        self.assertEqual(BinarySearch().search([1, 2, 3, 4,5,6,8,12,15], 5), 4)
    def test_binary_four(self):
        self.assertEqual(BinarySearch().search([1, 2, 3, 4,5,6,8,12,15], 15), 8)
    def test_binary_five(self):
        self.assertEqual(BinarySearch().search([], 1), -1)               
if __name__ == '__main__':
    unittest.main()
