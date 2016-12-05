import unittest

from src.other_technologies import cubed_list, other_cubed_list


class TestCubedList(unittest.TestCase):

    def test_equality(self):
        test_list = [2, 3, 4]
        self.assertEqual(cubed_list(test_list), [8, 27, 64])


class TestOtherCubedList(unittest.TestCase):

    def test_equality(self):
        test_list = [2, 3, 4]
        self.assertEqual(other_cubed_list(test_list), [8, 27, 64])


if __name__ == '__main__':
    unittest.main()
