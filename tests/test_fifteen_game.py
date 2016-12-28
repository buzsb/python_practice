import unittest

from src.fifteen_game import FifteenGame

a = FifteenGame(2, 2)


class FifteenGameTest(unittest.TestCase):

    def test_generated_list(self):
        self.assertEqual(len(a.generated_list(4)), 2)

    def test_empty_coordinates(self):
        a.field = [[1, 2], [3, '']]
        a.empty_coordinates()
        self.assertEqual(a.empty_x, 1)
        self.assertEqual(a.empty_y, 1)

    def test_swap_function(self):
        a.field = [[1, 2], [3, '']]
        a.swap(1, 1, 0, 1)
        swap_field = [[1, ''], [3, 2]]
        self.assertEqual(a.field, swap_field)

    def test_move_up(self):
        a.field = [[1, 2], ['', 3]]
        moved_field = [['', 2], [1, 3]]
        a.empty_coordinates()
        a.move_up()
        self.assertEqual(a.field, moved_field)

    def test_false_move_up(self):
        a.field = [['', 1], [2, 3]]
        self.assertFalse(a.move_up())

    def test_move_down(self):
        a.field = [[1, ''], [2, 3]]
        moved_field = [[1, 3], [2, '']]
        a.empty_coordinates()
        a.move_down()
        self.assertEqual(a.field, moved_field)

    def test_false_move_down(self):
        a.field = [[1, 2], ['', 3]]
        self.assertFalse(a.move_down())

    def test_move_left(self):
        a.field = [[1, ''], [2, 3]]
        moved_field = [['', 1], [2, 3]]
        a.empty_coordinates()
        a.move_left()
        self.assertEqual(a.field, moved_field)

    def test_false_move_left(self):
        a.field = [['', 1], [2, 3]]
        self.assertFalse(a.move_left())

    def test_move_right(self):
        a.field = [[1, 2], ['', 3]]
        moved_field = [[1, 2], [3, '']]
        a.empty_coordinates()
        a.move_right()
        self.assertEqual(a.field, moved_field)

    def test_false_move_right(self):
        a.field = [[1, 2], [3, '']]
        self.assertFalse(a.move_right())

    def test_win_check_true(self):
        a.field = [[1, 2], [3, '']]
        self.assertTrue(a.win_check())

    def test_win_check_false(self):
        a.field = [[1, 2], ['', 3]]
        self.assertFalse(a.win_check())


if __name__ == '__main__':
    unittest.main()
