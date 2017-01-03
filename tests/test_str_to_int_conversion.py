import unittest

from src.str_to_int_conversion import integer_conversion


class IntegerConversionTests(unittest.TestCase):

    def test_equality(self):
        test_string = '123'
        self.assertEqual(integer_conversion(test_string), 123)

    def test_second_equality(self):
        test_string = '34905'
        self.assertEqual(integer_conversion(test_string), 34905)

    def test_string_with_leters(self):
        test_string = '12l3'
        with self.assertRaises(ValueError):
            integer_conversion(test_string)

    def test_second_string_with_leters(self):
        test_string = '32i67k'
        with self.assertRaises(ValueError):
            integer_conversion(test_string)


if __name__ == '__main__':
    unittest.main()
