import unittest

from src.generators import range_generator, list_from_generator


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


class IteratorTest(unittest.TestCase):

    def test_equality(self):
        final_list = [0, 1, 2, 3]
        self.assertEqual(list_from_generator(range_generator(4)), final_list)

    def test_second_equality(self):
        final_list = [3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(
            list_from_generator(range_generator(3, 10)), final_list
        )


if __name__ == '__main__':
    unittest.main()
