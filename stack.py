class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return not self.items()

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
