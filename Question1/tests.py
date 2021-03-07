import unittest
import code

class TestCode(unittest.TestCase):
    def test_counting(self):
        self.assertEqual(code.fizz_buzz(1,3), '1, 2, 3')
        
if __name__ == '__main__':
    
    unittest.main()