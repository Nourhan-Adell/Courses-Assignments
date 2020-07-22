""" implementation of the linked-list """


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def print_node(self):
        print(self.data)


class Linked_List:
    def __init__(self):
        self.head = None

    def append_node(self, data):
        if not self.head:
            self.head = Node(data)
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next


a_node = Node("Sunday")
a_node.print_node()
lk = Linked_List()
lk.append_node("Monday")
lk.append_node("Tuesday")
lk.print_list()
