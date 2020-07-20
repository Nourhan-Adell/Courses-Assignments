def same(first, second):
    return (first is second)


class Square:
    def __init__(self):
        pass


obj = Square()
object = Square()

same(obj, object)
