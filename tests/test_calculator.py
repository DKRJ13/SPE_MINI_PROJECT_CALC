import os
import sys
import unittest
import math

# Ensure project root is on sys.path so tests can import the `src` package
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src import calculator


class TestCalculator(unittest.TestCase):

    def test_sqrt_positive(self):
        self.assertAlmostEqual(calculator.sqrt(9), 3.0)

    def test_sqrt_zero(self):
        self.assertAlmostEqual(calculator.sqrt(0), 0.0)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            calculator.sqrt(-1)

    def test_factorial_small(self):
        self.assertEqual(calculator.factorial(5), 120)

    def test_factorial_zero(self):
        self.assertEqual(calculator.factorial(0), 1)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            calculator.factorial(-3)

    def test_factorial_non_int(self):
        with self.assertRaises(TypeError):
            calculator.factorial(3.5)

    def test_ln_positive(self):
        self.assertAlmostEqual(calculator.ln(math.e), 1.0)

    def test_ln_non_positive(self):
        with self.assertRaises(ValueError):
            calculator.ln(0)

    def test_power(self):
        self.assertAlmostEqual(calculator.power(2, 3), 8.0)


if __name__ == '__main__':
    unittest.main()
