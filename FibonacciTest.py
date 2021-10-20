import unittest
from Fibonacci import Fibonacci

class FibonacciTest(unittest.TestCase):
    def test_fibonacci_one(self):
        self.assertEqual(Fibonacci().fibonacci(-1), "Invalid Input")
    def test_fibonacci_two(self):
        self.assertEqual(Fibonacci().fibonacci(2), 1)
    def test_fibonacci_four(self):
        self.assertEqual(Fibonacci().fibonacci(4), 3)
    def test_fibonacci_six(self):
        self.assertEqual(Fibonacci().fibonacci(6), 8)
    def test_fibonacci_seven(self):
        self.assertEqual(Fibonacci().fibonacci(7), 13)
    
        
        
if __name__ == '__main__':
    unittest.main()
