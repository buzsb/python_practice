def range_generator(end):
    i = 0
    while i <= end:
        yield i
        i += 1


if __name__ == '__main__':
    for x in range_generator(5):
        print x
