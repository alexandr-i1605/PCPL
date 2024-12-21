import unittest
from main import get_coeff, solv

class Test(unittest.TestCase):
    
    def test_1(self):
        with self.assertRaises(ValueError):
            get_coeff("abc", "A")
    
    def test_2(self):
        self.assertEqual(solv(1, 1, 1), [])
    
    def test_3(self):
        self.assertEqual(solv(1, 1, -2), [-1.0, 1.0])
    
    def test_4(self):
        self.assertEqual(solv(1, -10, 9), [-3.0, -1.0, 1.0, 3.0])

if __name__ == "__main__":
    unittest.main()
