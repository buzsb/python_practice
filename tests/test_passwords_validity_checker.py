import unittest

from src.passwords_validity_checker import password_validity_checker


class PasswordValidityCheckerTest(unittest.TestCase):

    def test_correct_work(self):
        passwords = 'password, 1111, P23Una#jd, GoodPass1$'
        result = ['P23Una#jd', 'GoodPass1$']
        self.assertListEqual(
            password_validity_checker(passwords), result
        )

    def test_empty_string(self):
        passwords = ''
        result = []
        self.assertListEqual(
            password_validity_checker(passwords), result
        )

    def test_one_char_string(self):
        passwords = 'x'
        result = []
        self.assertListEqual(
            password_validity_checker(passwords), result
        )

    def test_too_long_pasword(self):
        passwords = 'LongGoodPassword1$'
        result = []
        self.assertListEqual(
            password_validity_checker(passwords), result
        )

    def test_pasword_without_numbers(self):
        passwords = 'GoodPass$'
        result = []
        self.assertListEqual(
            password_validity_checker(passwords), result
        )

    def test_pasword_without_big_chars(self):
        passwords = 'goodpass1$'
        result = []
        self.assertListEqual(
            password_validity_checker(passwords), result
        )

    def test_pasword_without_smal_chars(self):
        passwords = '234456AA1$'
        result = []
        self.assertListEqual(
            password_validity_checker(passwords), result
        )

    def test_pasword_without_symbols(self):
        passwords = 'goodpass1'
        result = []
        self.assertListEqual(
            password_validity_checker(passwords), result
        )


if __name__ == '__main__':
    unittest.main()
