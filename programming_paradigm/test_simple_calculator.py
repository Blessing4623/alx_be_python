import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(SimpleCalculator.add(self, 2, 4), 6)
        self.assertEqual(SimpleCalculator.add(self, -3, 3), 0)
    def test_subtraction(self):
        self.assertEqual(SimpleCalculator.subtract(self, 7, 5), 2)
        self.assertEqual(SimpleCalculator.subtract(self, 4, 1), 3)
    def test_multiplication(self):
        self.assertEqual(SimpleCalculator.multiply(self, 5, 5), 25)
        self.assertEqual(SimpleCalculator.multiply(self, 4, 3), 12)
    def test_division(self):
        self.assertEqual(SimpleCalculator.divide(self, 9, 3), 3)
        self.assertEqual(SimpleCalculator.divide(self, 5, 0), None)

if __name__ == "__main__":
    unittest.main()