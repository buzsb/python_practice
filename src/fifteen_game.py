import random


class FifteenGame(object):

    def __init__(self, height=4, length=4):
        self.height = height
        self.length = length
        self.field = self.generated_list(self.height * self.length)

    def generated_list(self, number):
        array = range(number)
        random.shuffle(array)
        array[array.index(0)] = ''
        field = []
        for i in xrange(0, len(array), self.length):
            field.append(array[i:i + self.length])
        return field

    def print_field(self):
        for row in self.field:
            print ''.join(['{:>3}'.format(item) for item in row])

    def move_up(self):
        coordinates = []
        for i in self.field:
            if '' in i:
                coordinates.append(self.field.index(i))
                coordinates.append(i.index(''))
        x = coordinates[0]
        y = coordinates[1]
        if x == 0:
            return False
        self.field[x][y], self.field[x - 1][y] = self.field[x - 1][y], self.field[x][y]
        self.print_field()


if __name__ == '__main__':
    a = FifteenGame()
    a.print_field()
    a.move_up()
