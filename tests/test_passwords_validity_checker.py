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

    def test_parametr_is_number(self):
        passwords = 123
        self.assertIsNone(password_validity_checker(passwords))

    def test_parametr_list(self):
        passwords = [1, 2, 3]
        self.assertIsNone(password_validity_checker(passwords))

    def test_parametr_is_dict(self):
        passwords = {'a': 1, 'b': 2}
        self.assertIsNone(password_validity_checker(passwords))


if __name__ == '__main__':
    unittest.main()
