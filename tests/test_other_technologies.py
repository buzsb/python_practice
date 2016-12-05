import unittest

from src.other_technologies import cubed_list, other_cubed_list, \
    bigger_than_n, other_bigger_than_n


class TestCubedList(unittest.TestCase):

    def test_equality(self):
        test_list = [2, 3, 4]
        self.assertEqual(cubed_list(test_list), [8, 27, 64])


class TestOtherCubedList(unittest.TestCase):

    def test_equality(self):
        test_list = [2, 3, 4]
        self.assertEqual(other_cubed_list(test_list), [8, 27, 64])


class TestBiggerThanN(unittest.TestCase):

    def test_equality(self):
        test_list = [3, 4, 7, 8]
        self.assertEqual(bigger_than_n(test_list, 5), [7, 8])


class TestOtherBiggerThanN(unittest.TestCase):

    def test_equality(self):
        test_list = [3, 4, 7, 8]
        self.assertEqual(other_bigger_than_n(test_list, 5), [7, 8])


if __name__ == '__main__':
    unittest.main()
