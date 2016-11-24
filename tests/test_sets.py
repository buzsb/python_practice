import unittest

from src.sets import unique_elements_in_list


class UniqueElementsInListTest(unittest.TestCase):

    def test_equality(self):
        test_list = [1, 1, 2, 3, 3]
        self.assertEqual(sorted(unique_elements_in_list(test_list)), [1, 2, 3])

        second_test_list = [4, 4, 5, 3, 5]
        self.assertEqual(sorted(unique_elements_in_list(second_test_list)), [3, 4, 5])

    def test_second_equality(self):
        test_list = [2, 2, 3, 4, 3]

        def list_check(main_list):
            unique_elements_list = unique_elements_in_list(test_list)
            for i in unique_elements_list:
                if i not in main_list:
                    return False
            return True

        self.assertTrue(list_check(test_list))

    def test_short_true_check(self):
        test_list = [3, 4, 4, 5]
        unique_elements_list = unique_elements_in_list(test_list)

        self.assertTrue(all(i in test_list for i in unique_elements_list))


if __name__ == '__main__':
    unittest.main()
