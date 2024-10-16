from threading import Condition
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.c = Condition()
        self.count = 0
        self.capacity = capacity
        self.head = 0
        self.q = [-1] * capacity
        

    def enqueue(self, element: int) -> None:
        with self.c:
            while self.count == self.capacity:
                self.c.wait()
            self.q[(self.head + self.count) % self.capacity] = element
            self.count += 1
            self.c.notify()

        

    def dequeue(self) -> int:
        with self.c:
            while self.count < 1:
                self.c.wait()
            val = self.q[self.head]
            self.head = (self.head + 1) % self.capacity
            self.count -= 1
            self.c.notify()
        return val
        

    def size(self) -> int:
        return self.count
        