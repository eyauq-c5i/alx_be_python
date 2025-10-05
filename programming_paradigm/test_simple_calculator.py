import unittest

try:
    from simple_calculator import SimpleCalculator
except ImportError:
    print("Error: Could not find 'simple_calculator.py'. Ensure it is in the same directory.")
    import sys; sys.exit(1)


class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for the SimpleCalculator class, ensuring all arithmetic 
    operations function correctly across various scenarios.
    """

    def setUp(self):
        """Set up the SimpleCalculator instance before each individual test method."""
        self.calc = SimpleCalculator()

    def test_add_positive_numbers(self):
        """Test addition with two positive integers."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(100, 200), 300)

    def test_add_negative_numbers(self):
        """Test addition with two negative integers."""
        self.assertEqual(self.calc.add(-5, -5), -10)
        self.assertEqual(self.calc.add(-10, -3), -13)

    def test_add_mixed_numbers(self):
        """Test addition with a positive and a negative integer."""
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(50, -20), 30)

    def test_add_float_numbers(self):
        """Test addition with floating point numbers."""
        self.assertAlmostEqual(self.calc.add(1.5, 2.5), 4.0)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3)
    
    def test_add_with_zero(self):
        """Test addition where one of the operands is zero."""
        self.assertEqual(self.calc.add(7, 0), 7)
        self.assertEqual(self.calc.add(0, -3), -3)


    def test_subtract_positive_numbers(self):
        """Test subtraction with two positive integers."""
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(5, 10), -5)

    def test_subtract_negative_numbers(self):
        """Test subtraction involving negative integers."""
        self.assertEqual(self.calc.subtract(-5, -2), -3) # -5 - (-2) = -3
        self.assertEqual(self.calc.subtract(-10, 5), -15) # -10 - 5 = -15

    def test_subtract_with_zero(self):
        """Test subtraction where one of the operands is zero."""
        self.assertEqual(self.calc.subtract(15, 0), 15)
        self.assertEqual(self.calc.subtract(0, 8), -8)
        
    def test_subtract_float_numbers(self):
        """Test subtraction with floating point numbers."""
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.subtract(10.0, 0.5), 9.5)


    def test_multiply_positive_numbers(self):
        """Test multiplication with two positive integers."""
        self.assertEqual(self.calc.multiply(6, 7), 42)
        self.assertEqual(self.calc.multiply(10, 10), 100)

    def test_multiply_mixed_numbers(self):
        """Test multiplication with positive and negative integers."""
        self.assertEqual(self.calc.multiply(-5, 5), -25)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_multiply_by_zero(self):
        """Test multiplication where one of the factors is zero (edge case)."""
        self.assertEqual(self.calc.multiply(100, 0), 0)
        self.assertEqual(self.calc.multiply(0, -50), 0)

    def test_multiply_float_numbers(self):
        """Test multiplication with floating point numbers."""
        self.assertAlmostEqual(self.calc.multiply(2.5, 2.0), 5.0)
        self.assertAlmostEqual(self.calc.multiply(1.5, 3), 4.5)


    def test_divide_normal_division(self):
        """Test division where the result is an integer or float."""
        self.assertEqual(self.calc.divide(10, 5), 2.0)
        self.assertEqual(self.calc.divide(1, 2), 0.5)

    def test_divide_negative_numbers(self):
        """Test division involving negative numbers."""
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(-10, -5), 2.0)
        
    def test_divide_by_zero(self):
        """Test the crucial edge case: division by zero."""
        # The SimpleCalculator returns None for division by zero
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))

    def test_divide_zero_by_number(self):
        """Test dividing zero by a non-zero number."""
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -10), 0.0)

# This block allows the script to be run from the command line
if __name__ == '__main__':
    unittest.main()