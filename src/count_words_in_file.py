import os.path
from collections import defaultdict


def file_lines_to_words_list_converter(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as file:
        text = file.read()
    words_list = []
    start_word = 0
    for i, char in enumerate(text):
        if ord(char) < ord('A') or ord(char) > ord('z'):
            word = text[start_word:i]
            start_word = i + 1
            if word != '':
                words_list.append(word)
    return words_list


def words_counter(words_list):
    repeated_words_dict = defaultdict(int)
    for word in words_list:
        word = word.lower()
        repeated_words_dict[word] += 1
    list_of_repeated_words = repeated_words_dict.items()
    sorted_list_of_repeated_words = sorted(
        list_of_repeated_words, key=lambda tup: tup[1], reverse=True
    )
    return sorted_list_of_repeated_words[:3]


if __name__ == '__main__':
    print words_counter(file_lines_to_words_list_converter('text_file.txt'))
