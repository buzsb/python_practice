import unittest

from src.repeated_words import repeated_words


class TestRepeatWords(unittest.TestCase):

    def test_equality(self):
        test_list = ['cat', 'Cat', 'doG', 'dog', 'COW']
        self.assertEqual(len(repeated_words(test_list)), 2)

    def test_second_equality(self):
        test_list = ['cat', 'doG', 'COW']
        self.assertEqual(len(repeated_words(test_list)), 0)

    def test_empty_list(self):
        test_list = []
        self.assertEqual(len(repeated_words(test_list)), 0)


if __name__ == '__main__':
    unittest.main()
