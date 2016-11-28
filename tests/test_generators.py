import unittest

from src.generators import range_generator


class RangeGeneratorTest(unittest.TestCase):

    def test_equality(self):
        test_list = []
        for i in range_generator(5):
            test_list.append(i)
        self.assertEqual(test_list, range(5))

    def test_second_equality(self):
        test_list = []
        for i in range_generator(3, 9):
            test_list.append(i)
        self.assertEqual(test_list, range(3, 9))


if __name__ == '__main__':
    unittest.main()
