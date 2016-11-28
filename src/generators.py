def range_generator(start, end=None):
    if end is None:
        end = start
        start = 0
    while start < end:
        yield start
        start += 1


if __name__ == '__main__':
    for x in range_generator(5):
        print x
