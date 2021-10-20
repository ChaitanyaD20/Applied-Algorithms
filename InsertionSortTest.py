import unittest
from InsertionSort import InsertionSort

class InsertionSortTest(unittest.TestCase):
    def test_insertionsort_one(self):
        self.assertEqual(InsertionSort().insertionsort([3,5,1,6,4]), [1,3,4,5,6])
    def test_insertionsort_two(self):
        self.assertEqual(InsertionSort().insertionsort([-1,3,2,6,-13]),[-13,-1,2,3,6])
    def test_insertionsort_four(self):
        self.assertEqual(InsertionSort().insertionsort([0,1,2,4,10000]), [0,1,2,4,10000])
    def test_insertionsort_six(self):
        self.assertEqual(InsertionSort().insertionsort([14,13,12,11,6,1]), [1,6,11,12,13,14])
    
        
        
if __name__ == '__main__':
    unittest.main()
