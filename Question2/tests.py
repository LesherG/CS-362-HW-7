import unittest
import code


class TestCode(unittest.TestCase):
    def test_non4multiples(self):
        self.assertFalse(code.leap_year(3))
        self.assertFalse(code.leap_year(6))
        
    def test_mult_of_4_non100(self):
        self.assertTrue(code.leap_year(4))
        self.assertTrue(code.leap_year(16))
        
        
if __name__ == '__main__':
    unittest.main()