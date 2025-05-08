from collections import deque
class Steck():
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

ste = Steck()

print(ste.is_empty())
print(ste.pop())
print(ste.push())
print(ste.size())
