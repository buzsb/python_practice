import unittests

from src.sets import unique_elements_in_list


class UniqueElementsInListTest(unittest.TestCase):

    def test_equality(self):
        test_list = [1, 1, 2, 3, 3]
        self.assertEqual(unique_elements_in_list(test_list), [1, 2, 3])

        second_test_list = [4, 4, 5, 3, 5]
        self.assertEqual(unique_elements_in_list(second_test_list), [3, 4, 5])


if __name__ == '__main__':
    unittest.main()