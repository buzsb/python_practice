def range_generator(start, end=None):
    if end is None:
        end = start
        start = 0
    while start < end:
        yield start
        start += 1


def list_from_generator(generator):
    generated_list = []
    while True:
        try:
            i = generator.next()
            generated_list.append(i)
        except StopIteration:
            break
    return generated_list


if __name__ == '__main__':
    for x in range_generator(5):
        print x

    print list_from_generator(range_generator(3, 10))
