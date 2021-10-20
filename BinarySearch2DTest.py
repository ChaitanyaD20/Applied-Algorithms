import unittest
from BinarySearch2D import BinarySearch2D

class BinarySearch2DTest(unittest.TestCase):
    def test_binary2d_one(self):
        M = [[1, 3, 4, 5],
             [5, 6, 7, 7],
             [8, 10, 11, 12],
             [12, 13, 15, 16]]
        q = 90
        (i, j) = BinarySearch2D().search(M, q)
        self.assertEqual([-1,1], q)

if __name__ == '__main__':
    unittest.main()