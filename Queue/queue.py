
from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, value):
        self.buffer.appendleft(value)
    
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
    def front(self):
        return self.buffer[-1]


if __name__=="__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue(8)
    q.enqueue(12)
    print(q.buffer)
    print(q.dequeue())