import unittest

from src.classes import Square, SquareWithColor


class TestSquareClass(unittest.TestCase):

    def test_equality(self):
        a = Square(5)
        self.assertEqual(a.square_area(), 25)


class TestSquareWithColor(unittest.TestCase):

    def test_equaity(self):
        b = SquareWithColor(4, 'red')
        self.assertEqual(b.square_area(), 16)


if __name__ == '__main__':
    unittest.main()
