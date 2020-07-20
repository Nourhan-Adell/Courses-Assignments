class Square:
    def __init__(self, side):
        self.side = side
        pass

    def perimeter(self):
        return 4 * self.side

    def __repr__(self):
        return ("{} by {} by {} by {}".format(self.side, self.side, self.side, self.side))


print(Square(29))
