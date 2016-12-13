import unittest

from src.regular_expressions import first_crt_uppercase, \
    last_crt_number, is_there_only_love


class FirstCrtUppercaseTest(unittest.TestCase):

    def test_correct_work(self):
        string = 'Test string'
        self.assertTrue(first_crt_uppercase(string))

    def test_return_none(self):
        string = 'test string'
        self.assertFalse(first_crt_uppercase(string))


class LastCrtNumberTest(unittest.TestCase):

    def test_correct_work(self):
        string = 'Test string 1'
        self.assertTrue(last_crt_number(string))

    def test_return_none(self):
        string = 'test string'
        self.assertFalse(last_crt_number(string))


class IsThereOnlyLoveTest(unittest.TestCase):

    def test_correct_work(self):
        string = 'lovve'
        self.assertTrue(is_there_only_love(string))

    def test_return_none(self):
        string = 'what is love baby dont hurt me'
        self.assertFalse(is_there_only_love(string))


if __name__ == '__main__':
    unittest.main()
