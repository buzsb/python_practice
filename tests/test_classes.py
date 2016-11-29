import unittest

from src.classes import Square


class TestSquareClass(unittest.TestCase):

    def test_equality(self):
        a = Square(5)
        self.assertEqual(a.square_area(), 25)


if __name__ == '__main__':
    unittest.main()
