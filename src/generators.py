def range_generator(start, end=None):
    if end is None:
        end = start
        start = 0
    while start < end:
        yield start
        start += 1


def iterator(generator):
    generated_list = []
    try:
        while True:
            i = generator.next()
            generated_list.append(i)
    except StopIteration:
        pass
    return generated_list


if __name__ == '__main__':
    for x in range_generator(5):
        print x

    print iterator(range_generator(3, 10))
