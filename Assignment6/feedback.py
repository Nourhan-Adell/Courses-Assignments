class Shape():

    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a shape")


class Rectangle(Shape):

    def __init__(self, w, l):
        self.width = w

        self.length = l

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


class Square(Shape):

    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, number):
        self.s1 += number

    def print_size(self):
        return self.s1


sh1 = Rectangle(10, 5)

sh2 = Square(3)

sh1.what_am_i()

sh2.what_am_i()
