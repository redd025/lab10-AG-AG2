#https://github.com/redd025/lab10-AG-AG2
# Partner 1: Alexander Gordillo Jimenez

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-4, 5), 1)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(0,0), 0)
        self.assertEqual(subtract(-2,-3), 1)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 2), 4)
        self.assertEqual(mul(0, 3), 0)
        self.assertEqual(mul(-3, 1), -3)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(3, 6), 2)
        self.assertAlmostEqual(div(5, 10), 2.0)
        self.assertEqual(div(1, -5), -5)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0,5)

    def test_logarithm(self): # 3 assertions
        with self.assertRaises(ValueError):
            logarithm(0, 3)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-3,4)
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(6, 8), 10)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
           square_root(-9)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(25), 5)


# Do not touch this
if __name__ == "__main__":
    unittest.main()