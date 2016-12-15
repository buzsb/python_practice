import random


def generated_list(number):
    array = range(number)
    random.shuffle(array)
    return array


def fifteenki(height=4, length=4):
    generated_lst = generated_list(height * length)
    matrix = []
    for i in xrange(0, len(generated_lst), length):
        matrix.append(generated_lst[i:i + length])
    print matrix
    for row in matrix:
        for colunm in row:
            print ('{:>3}').format(colunm)
        print


if __name__ == '__main__':
    fifteenki()
