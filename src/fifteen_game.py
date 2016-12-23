import random


class FifteenGame(object):

    def __init__(self, height=4, length=4):
        self.height = height
        self.length = length
        self.field = self.generated_list(self.height * self.length)

    def generated_list(self, number):
        array = range(number)
        random.shuffle(array)
        return array

    def print_field(self):
        self.field[self.field.index(0)] = ''
        matrix = []
        for i in xrange(0, len(self.field), self.length):
            matrix.append(self.field[i:i + self.length])
        for row in matrix:
            print ''.join(['{:>3}'.format(item) for item in row])


if __name__ == '__main__':
    a = FifteenGame()
    a.print_field()
