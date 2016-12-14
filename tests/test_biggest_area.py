import unittest
from src.biggest_area import biggest_area


class BiggestAreaTest(unittest.TestCase):

    def test_equality(self):
        test_array = [1, 2, 3, 4]
        self.assertEqual(biggest_area(test_array), 6)

    def test_second_equality(self):
        test_array = [4, 2, 3, 4]
        self.assertEqual(biggest_area(test_array), 8)


if __name__ == '__main__':
    unittest.main()
