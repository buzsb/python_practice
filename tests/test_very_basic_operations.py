import unittest

from src.very_basic_operations import add, factorial


class AddingTwoNumbersTest(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(0, 3), 3)
        self.assertEqual(add(-1, 3), 2)


class FactorialTest(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)

    def test_argument_float(self):
        with self.assertRaisesRegexp(ValueError, "Number is not integral."):
            factorial(1.5)

    def test_argument_less_than_zero(self):
        with self.assertRaisesRegexp(ValueError, "Number is less than 0."):
            factorial(-3)

if __name__ == '__main__':
    unittest.main()