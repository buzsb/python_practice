def file_lines_to_words_list_converter():
    file = open("src/text_file.txt")
    words_list = []
    text = ''.join(file.readlines())
    start_word = 0
    for i, digit in enumerate(text):
        if ord(digit) < ord('A') or ord(digit) > ord('z'):
            word = text[start_word:i]
            words_list.append(word)
            start_word = i + 1
    return words_list


if __name__ == '__main__':
    print file_lines_to_words_list_converter()
