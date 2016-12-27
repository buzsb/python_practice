import random


class FifteenGame(object):

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.field = self.generated_list(self.height * self.width)
        self.empty_coordinates()

    def generated_list(self, number):
        array = range(number)
        random.shuffle(array)
        array[array.index(0)] = ''
        field = []
        for i in xrange(0, len(array), self.width):
            field.append(array[i:i + self.width])
        return field

    def print_field(self):
        for row in self.field:
            print ''.join(['{:>3}'.format(item) for item in row])

    def empty_coordinates(self):
        for i in self.field:
            if '' in i:
                self.empty_y = self.field.index(i)
                self.empty_x = i.index('')
                break

    def swap(self, y1, x1, y2, x2):
        self.field[y1][x1], self.field[y2][x2] = (
            self.field[y2][x2], self.field[y1][x1])

    def move_up(self):
        if self.empty_y == 0:
            return False
        self.swap(self.empty_y, self.empty_x, self.empty_y - 1, self.empty_x)

        self.empty_y = self.empty_y - 1

    def move_down(self):
        if self.empty_y == self.height - 1:
            return False
        self.swap(self.empty_y, self.empty_x, self.empty_y + 1, self.empty_x)

        self.empty_y = self.empty_y + 1

    def move_left(self):
        if self.empty_x == 0:
            return False
        self.swap(self.empty_y, self.empty_x - 1, self.empty_y, self.empty_x)

        self.empty_x = self.empty_x - 1

    def move_right(self):
        if self.empty_x == self.width - 1:
            return False
        self.swap(self.empty_y, self.empty_x + 1, self.empty_y, self.empty_x)

        self.empty_x = self.empty_x + 1

    def win_check(self):
        for y, row in enumerate(self.field):
            for x, number in enumerate(row):
                if number == '':
                    continue
                if number != y * self.width + x + 1:
                    return False
        return True


def play_game(height=4, width=4):
    a = FifteenGame(height, width)
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
        a.print_field()
        if a.win_check():
            break
        if move == 'e':
            break


if __name__ == '__main__':
    play_game()
