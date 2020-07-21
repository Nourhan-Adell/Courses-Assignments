"""
    implementing Queue
    we also can use the package that include Queue
"""


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


a_queue = Queue()
print(a_queue.is_empty())
for i in range(0, 11):
    a_queue.enqueue(i)
print(a_queue.items)

for i in range(a_queue.size()):
    print(i)
