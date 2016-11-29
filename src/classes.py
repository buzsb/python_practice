class Square(object):

    def __init__(self, length):
        self.length = length

    def square_area(self):
        return self.length * self.length


if __name__ == '__main__':
    a = Square(5)
    print a.square_area()
