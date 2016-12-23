import random


class FifteenkiGame(object):

    def __init__(self, height=4, length=4):
        self.height = height
        self.length = length

    def generated_list(self, number):
        array = range(number)
        random.shuffle(array)
        return array

    def fifteenki(self):
        array = self.generated_list(self.height * self.length)
        array[array.index(0)] = ''
        matrix = []
        for i in xrange(0, len(array), self.length):
            matrix.append(array[i:i + self.length])
        for row in matrix:
            print ''.join(['{:>3}'.format(item) for item in row])


if __name__ == '__main__':
    a = FifteenkiGame()
    a.fifteenki()
