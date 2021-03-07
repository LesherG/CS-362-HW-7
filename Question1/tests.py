import unittest
import code

class TestCode(unittest.TestCase):
    def test_counting(self):
        self.assertEqual(code.fizz_buzz(1,2), '1, 2')
        
    def test_fizz(self):
        self.assertEqual(code.fizz_buzz(2,4), '2, Fizz, 4')
        
if __name__ == '__main__':
    
    unittest.main()