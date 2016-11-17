import unittest

from src.max_number_occurence import generated_dictionary, max_number_occurence


class GerneratedDictionaryTest(unittest.TestCase):

    def test_equal_type(self):
        self.assertEqual(type(generated_dictionary()), dict)


if __name__ == '__main__':
    unittest.main()