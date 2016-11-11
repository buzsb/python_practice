import unittest

from src.very_basic_operations import add


class AddingTwoNumbersTest(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(0, 3), 3)
        self.assertEqual(add(-1, 3), 2)

if __name__ == '__main__':
    unittest.main()