class Square:

    def __init__(self, side):
        self.s1 = side

    def perimeter(self):
        return self.s1 * 4

    def change_size(self, new_size):
        self.s1 = self.s1 + new_size
    
