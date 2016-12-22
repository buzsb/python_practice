import unittest

from src.repeated_words import repeated_words


class TestRepeatWords(unittest.TestCase):

    def test_equality(self):
        test_list = ['cat', 'Cat', 'doG', 'dog', 'COW']
        repeated = set(['cat', 'dog'])
        self.assertEqual(repeated_words(test_list), repeated)

    def test_second_equality(self):
        test_list = ['cat', 'doG', 'COW']
        repeated = set()
        self.assertEqual(repeated_words(test_list), repeated)

    def test_empty_list(self):
        test_list = []
        repeated = set()
        self.assertEqual(repeated_words(test_list), repeated)


if __name__ == '__main__':
    unittest.main()
