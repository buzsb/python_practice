import unittest
from src.binary_search import binary_search, \
    recursive_binary_search, another_recursive_binary_search


class BinarySearchTest(unittest.TestCase):

    def test_element_in_list(self):
        test_list = [1, 2, 3, 4]
        searched_element_index = test_list.index(3)
        self.assertEqual(binary_search(test_list, 3), searched_element_index)

    def test_element_not_in_list(self):
        test_list = [1, 2, 3, 4]
        self.assertIsNone(binary_search(test_list, 8))

    def test_list_with_one_searched_element(self):
        test_list = [3]
        searched_element_index = test_list.index(3)
        self.assertEqual(binary_search(test_list, 3), searched_element_index)

    def test_list_with_one_element(self):
        test_list = [3]
        self.assertIsNone(binary_search(test_list, 8))

    def test_empty_list(self):
        test_list = []
        self.assertIsNone(binary_search(test_list, 8))


class RecursiveBinarySearchTest(unittest.TestCase):

    def test_element_in_list_recursive(self):
        test_list = [1, 2, 3, 4]
        searched_element_index = test_list.index(3)
        self.assertEqual(
            recursive_binary_search(test_list, 3), searched_element_index)

    def test_element_not_in_list(self):
        test_list = [1, 2, 3, 4]
        self.assertIsNone(recursive_binary_search(test_list, 8))

    def test_list_with_one_searched_element(self):
        test_list = [3]
        searched_element_index = test_list.index(3)
        self.assertEqual(
            recursive_binary_search(test_list, 3), searched_element_index)

    def test_list_with_one_element(self):
        test_list = [3]
        self.assertIsNone(recursive_binary_search(test_list, 8))

    def test_empty_list(self):
        test_list = []
        self.assertIsNone(recursive_binary_search(test_list, 8))


class AnotherRecursiveBinarySearchTest(unittest.TestCase):

    def test_element_in_list_recursive(self):
        test_list = [1, 2, 3, 4]
        searched_element_index = test_list.index(3)
        self.assertEqual(
            another_recursive_binary_search(test_list, 3),
            searched_element_index
        )

    def test_element_not_in_list(self):
        test_list = [1, 2, 3, 4]
        self.assertIsNone(another_recursive_binary_search(test_list, 8))

    def test_list_with_one_searched_element(self):
        test_list = [3]
        searched_element_index = test_list.index(3)
        self.assertEqual(
            another_recursive_binary_search(test_list, 3),
            searched_element_index
        )

    def test_list_with_one_element(self):
        test_list = [3]
        self.assertIsNone(another_recursive_binary_search(test_list, 8))

    def test_empty_list(self):
        test_list = []
        self.assertIsNone(another_recursive_binary_search(test_list, 8))


if __name__ == '__main__':
    unittest.main()
