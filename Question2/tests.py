import unittest
import code


class TestCode(unittest.TestCase):
    def test_non4multiples(self):
        self.assertFalse(code.leap_year(3))
        self.assertFalse(code.leap_year(6))
        
        
if __name__ == '__main__':
    unittest.main()