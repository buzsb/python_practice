import unittest

from src.str_to_int_and_int_to_str_conversion import \
    conversion_string_to_integer, conversion_integer_to_string


class TestsConversionStringToInteger(unittest.TestCase):

    def test_equality(self):
        test_string = '123'
        self.assertEqual(conversion_string_to_integer(test_string), 123)

    def test_second_equality(self):
        test_string = '34905'
        self.assertEqual(conversion_string_to_integer(test_string), 34905)

    def test_string_with_leters(self):
        test_string = '12l3'
        with self.assertRaises(ValueError):
            conversion_string_to_integer(test_string)

    def test_second_string_with_leters(self):
        test_string = '32i67k'
        with self.assertRaises(ValueError):
            conversion_string_to_integer(test_string)


class TestsConversionIntegerToString(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(conversion_integer_to_string(123), '123')

    def test_second_equality(self):
        self.assertEqual(conversion_integer_to_string(34905), '34905')

    def test_type_equality(self):
        self.assertEqual(type(conversion_integer_to_string(34905)), str)


if __name__ == '__main__':
    unittest.main()
