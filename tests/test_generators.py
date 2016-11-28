import unittest

from src.generators import range_generator


class RangeGeneratogTest(unittest.TestCase):

    def test_equality(self):
        test_list = []
        for i in range_generator(5):
            test_list.append(i)
        self.assertEqual(test_list, range(5))


if __name__ == '__main__':
    unittest.main()
