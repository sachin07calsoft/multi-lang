import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(3, 2), 1)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 3), 2.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(1, 0)
