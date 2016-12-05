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

    def test_parameters_equality(self):
        b = SquareWithColor(6, 'blue')
        self.assertEqual(b.length, 6)
        self.assertEqual(b.color, 'blue')


if __name__ == '__main__':
    unittest.main()
