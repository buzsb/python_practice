import unittest

from src.shell_sort import shell_sort


class InsertionSortTest(unittest.TestCase):

    def test_correct_worc(self):
        unsorted_list = [5, 4, 3, 2, 1]
        sorted_list = [1, 2, 3, 4, 5]
        self.assertListEqual(shell_sort(unsorted_list), sorted_list)

    def test_second_correct_worc(self):
        unsorted_list = [3, 5, 1, 2, 4]
        sorted_list = [1, 2, 3, 4, 5]
        self.assertListEqual(shell_sort(unsorted_list), sorted_list)

    def test_empty_list(self):
        self.assertListEqual(shell_sort([]), [])


if __name__ == '__main__':
    unittest.main()
