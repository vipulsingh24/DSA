from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def peek(self):
        return self.items[0]
 
    def size(self):
        return len(self.items)

    def is_empty(self):
        return not self.items

    def __str__(self):
        return str(self.items)
