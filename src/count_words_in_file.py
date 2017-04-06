def file_reader():
    file = open("text_file.txt")
    for line in file:
        print line


if __name__ == '__main__':
    file_reader()
