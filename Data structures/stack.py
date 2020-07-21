"""
    implementing Stack
    we also can use the package that include stack
"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)


obj = Stack()
obj.push(1)
print(obj.is_empty())
for i in range(1, 11):
    obj.push(i)
print(obj.items)  # It prints the full Stack Or list at general
print(obj.size())
obj.pop()
print(obj.items)

print("\n *** Print the reversed of word 'Hello' ***** \n")
stack = Stack()
for c in "Hello":
    stack.push(c)
reversed_string = ""
for i in range(len(stack.items)):
    reversed_string += stack.pop()

print(reversed_string)
