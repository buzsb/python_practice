def range_generator(start, end):
    while start < end:
        yield start
        start += 1


if __name__ == '__main__':
    for x in range_generator(0, 5):
        print x
