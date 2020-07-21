"""
    using Queue to make a program that calculate the number of peoples than can buy a ticket till the movie starts

"""
import random
import time


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, new_item):
        self.items.insert(0, new_item)

    def dequeue(self):
        return self.items.pop()

    def simulation_line(self, time_till_show, max_time_for_tickets):
        obj1 = Queue()
        sold_tickets = []
        for i in range(100):
            obj1.enqueue("Person" + str(i))

        end_time = time.time() + time_till_show
        now_time = time.time()  # It give the current time

        while now_time < end_time and not obj1.is_empty():
            now_time = time.time()
            r = random.randint(0,
                               max_time_for_tickets)  # It select a random time between 0 sec to the maximum time when the movie starts
            time.sleep(r)  # sleep: is used to take the program stop or pause for a certain time
            person = obj1.dequeue()
            print(person)

            sold_tickets.append((person))

        return sold_tickets


q = Queue()
print(q.simulation_line(20, 2))
