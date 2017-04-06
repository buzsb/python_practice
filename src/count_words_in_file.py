def file_lines_to_words_list_converter():
    file = open("src/text_file.txt")
    words_list = []
    for line in file:
        line_list = line.split()
        for word in line_list:
            word = list(word)
            while ord(word[-1]) < ord('A') or ord(word[-1]) > ord('z'):
                word = word[:-1]
                if len(word) == 0:
                    break
            words_list.append(''.join(word))
    return words_list


if __name__ == '__main__':
    print file_lines_to_words_list_converter()
