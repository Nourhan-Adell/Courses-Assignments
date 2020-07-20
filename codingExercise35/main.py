class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return 2 * (self.width + self.length)


class Square():
    def __init__(self, one):
        self.one = one

    def calculate_perimeter(self):
        return 4 * self.one


rectangle = Rectangle(10, 20)
square = Square(10)

print(rectangle.calculate_perimeter())
print(square.calculate_perimeter())
