import unittest

from src.max_number_occurence import generated_dictionary, max_number_occurrence


class GerneratedDictionaryTest(unittest.TestCase):

    def test_correct_work(self):
        test_list = [1, 1, 2]
        self.assertEqual(generated_dictionary(test_list), {1:2, 2:1})

        second_test_list = [2, 3, 4, 2, 5]
        self.assertEqual(generated_dictionary(second_test_list), {2:2, 3:1, 4:1, 5:1})

    def test_empty_list(self):
        test_list = []
        self.assertEqual(generated_dictionary(test_list), {})

class MaxNumberOccurrenceTest(unittest.TestCase):

    def test_correct_work(self):
        test_list = [1, 1, 2]
        self.assertEqual(max_number_occurrence(test_list), (1, 2))

        second_test_list = [7, 3, 4, 6, 7, 9, 8, 6, 6, 4]
        self.assertEqual(max_number_occurrence(second_test_list), (6, 3))

    def test_empty_list(self):
        test_list = []
        with self.assertRaises(IndexError):
            max_number_occurrence(test_list)

if __name__ == '__main__':
    unittest.main()