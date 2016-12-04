class Square(object):

    def __init__(self, length):
        self.length = length

    def __repr__(self):
        return ('Square with length {length} has area {area}'
                .format(length=self.length, area=self.square_area())
                )

    def square_area(self):
        return self.length ** 2


class SquareWithColor(Square):

    def __init__(self, length, color):
        self.length = length
        self.color = color


if __name__ == '__main__':
    a = Square(5)
    print a.square_area()
    print a
    b = SquareWithColor(4, 'red')
    print b.square_area()
