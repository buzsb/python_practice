import random


def generated_list(number):
    array = range(number)
    random.shuffle(array)
    return array


def fifteenki(height=4, length=4):
    array = generated_list(height * length)
    array[array.index(0)] = ''
    matrix = []
    for i in xrange(0, len(array), length):
        matrix.append(array[i:i + length])
    for row in matrix:
        print ''.join(['{:>3}'.format(item) for item in row])


if __name__ == '__main__':
    fifteenki(7, 7)
