import unittest

from src.count_words_in_file import words_counter, \
    file_lines_to_words_list_converter


class FileLinesToWordsListConverterTest(unittest.TestCase):

    def test_correct_work(self):
        file_text_list = ['test', 'test', 'test', 'file', 'file', 'text']
        self.assertListEqual(
            file_lines_to_words_list_converter('../tests/test_text_file.txt'),
            file_text_list
        )


class WordCounterTest(unittest.TestCase):

    def test_correct_work(self):
        file_text_list = [('test', 3), ('file', 2), ('text', 1)]
        self.assertListEqual(
            words_counter(
                file_lines_to_words_list_converter('../tests/test_text_file.txt')
            ),
            file_text_list
        )


if __name__ == '__main__':
    unittest.main()
