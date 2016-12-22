import unittest

from src.fifteenki import generated_list


class TestGeneratedList(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(len(generated_list(16)), 16)

    def test_secont_equality(self):
        self.assertEqual(len(generated_list(9)), 9)


if __name__ == '__main__':
    unittest.main()
