import random


class FifteenGame(object):

    def __init__(self, height=4, length=4):
        self.height = height
        self.length = length
        self.field = self.generated_list(self.height * self.length)
        self.empty_coordinates()

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

    def empty_coordinates(self):
        for i in self.field:
            if '' in i:
                self.empty_y = self.field.index(i)
                self.empty_x = i.index('')

    def swap(self, y1, x1, y2, x2):
        self.field[y1][x1], self.field[y2][x2] = (
            self.field[y2][x2], self.field[y1][x1])

    def move_up(self):
        if self.empty_y == 0:
            return False
        self.swap(self.empty_y, self.empty_x, self.empty_y - 1, self.empty_x)

        self.empty_y = self.empty_y - 1
        self.print_field()

    def move_down(self):
        if self.empty_y == self.height - 1:
            return False
        self.swap(self.empty_y, self.empty_x, self.empty_y + 1, self.empty_x)

        self.empty_y = self.empty_y + 1
        self.print_field()

    def move_left(self):
        if self.empty_x == 0:
            return False
        self.swap(self.empty_y, self.empty_x - 1, self.empty_y, self.empty_x)

        self.empty_x = self.empty_x - 1
        self.print_field()

    def move_right(self):
        if self.empty_x == self.length - 1:
            return False
        self.swap(self.empty_y, self.empty_x + 1, self.empty_y, self.empty_x)

        self.empty_x = self.empty_x + 1
        self.print_field()


def play_game():
    a = FifteenGame()
    a.print_field()
    print (
        'Use w - to move up,\n'
        's - to move down,\n'
        'a - to move left,\n'
        'd - to move right,\n'
        'and e - to exit game\n'
    )
    while True:
        move = raw_input()
        if move == 'w':
            a.move_up()
        if move == 's':
            a.move_down()
        if move == 'a':
            a.move_left()
        if move == 'd':
            a.move_right()
        if move == 'e':
            break


if __name__ == '__main__':
    play_game()
