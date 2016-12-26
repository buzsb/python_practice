import random


class FifteenGame(object):

    def __init__(self, height=4, length=4):
        self.height = height
        self.length = length
        self.field = self.generated_list(self.height * self.length)
        self.x = 0
        self.y = 0

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

    def coordinates(self):
        for i in self.field:
            if '' in i:
                self.x = self.field.index(i)
                self.y = i.index('')

    def move_up(self):
        if self.x == 0:
            return False
        print ''
        self.field[self.x][self.y], self.field[self.x - 1][self.y] = (
            self.field[self.x - 1][self.y], self.field[self.x][self.y])

        self.x = self.x - 1
        self.print_field()

    def move_down(self):
        if self.x == len(self.field) - 1:
            return False
        print ''
        self.field[self.x][self.y], self.field[self.x + 1][self.y] = (
            self.field[self.x + 1][self.y], self.field[self.x][self.y])

        self.x = self.x + 1
        self.print_field()

    def move_left(self):
        if self.y == 0:
            return False
        print ''
        self.field[self.x][self.y], self.field[self.x][self.y - 1] = (
            self.field[self.x][self.y - 1], self.field[self.x][self.y])

        self.x = self.y - 1
        self.print_field()

    def move_right(self):
        if self.y == len(self.field[0]) - 1:
            return False
        print ''
        self.field[self.x][self.y], self.field[self.x][self.y + 1] = (
            self.field[self.x][self.y + 1], self.field[self.x][self.y])

        self.x = self.y + 1
        self.print_field()


if __name__ == '__main__':
    a = FifteenGame()
    a.coordinates()
    a.print_field()
    a.move_right()
