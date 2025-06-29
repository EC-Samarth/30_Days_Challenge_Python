#: Unit Testing with unittest
#1.Write tests for a calculator module

#calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

#2. Test exception handling and edge cases
import unittest
import calculator

class TestCalculator(unittest.TestCase):

    # Normal cases
    def test_add(self):
        self.assertEqual(calculator.add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(calculator.Substract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)

    # Edge cases
    def test_add_negative(self):
        self.assertEqual(calculator.add(-1, -1), -2)

    def test_divide_floats(self):
        self.assertAlmostEqual(calculator.divide(7, 3), 2.3333, places=4)

    # Exception handling
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.divide(10, 0)

if __name__ == "__main__":
    unittest.main()
