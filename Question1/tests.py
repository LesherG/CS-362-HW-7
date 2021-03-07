import unittest
import code

class TestCode(unittest.TestCase):
    def test_counting(self):
        self.assertEqual(code.fizz_buzz(1,2), '1, 2')
        
    def test_fizz(self):
        self.assertEqual(code.fizz_buzz(2,4), '2, Fizz, 4')
    
    def test_buzz(self):
        self.assertEqual(code.fizz_buzz(10,11), 'Buzz, 11')
        
    def test_fizzBuzz(self):
        self.assertEqual(code.fizz_buzz(10, 20), 'Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz')
        
if __name__ == '__main__':
    
    unittest.main()
    print(code.fizz_buzz(1,100))