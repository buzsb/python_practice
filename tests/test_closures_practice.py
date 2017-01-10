import unittest

from src.closures_practice import make_check_if_number_in_range


class NumberInRangeCheckTest(unittest.TestCase):

    def test_correct_work(self):
        tested_number = make_check_if_number_in_range(1, 10)
        self.assertTrue(tested_number(4))

    def test_second_correct_work(self):
        tested_number = make_check_if_number_in_range(6, 44)
        self.assertTrue(tested_number(12))

    def test_number_out_of_range(self):
        tested_number = make_check_if_number_in_range(1, 10)
        self.assertIsNone(tested_number(14))


if __name__ == '__main__':
    unittest.main()
