class Square(object):

    def __init__(self, length):
        self.length = length

    def __repr__(self):
        return ('Square with length {length} has area {area}'
                .format(length=self.length, area=self.length ** 2)
                )

    def square_area(self):
        return self.length ** 2


if __name__ == '__main__':
    a = Square(5)
    print a.square_area()
    print a.__repr__()
