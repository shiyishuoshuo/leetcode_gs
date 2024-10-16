from threading import Lock
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.q = [-1] * self.capacity
        self.en_lock, self.de_lock = Lock(), Lock()
        self.head, self.count = 0, 0
        self.de_lock.acquire()

        

    def enqueue(self, element: int) -> None:
        self.en_lock.acquire()
        self.q[(self.head + self.count) % self.capacity] = element
        self.count += 1
        if self.count < self.capacity:
            self.en_lock.release()
        if self.de_lock.locked():
            self.de_lock.release()

        

    def dequeue(self) -> int:
        self.de_lock.acquire()
        val = self.q[(self.head) % self.capacity]
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        if self.count > 0:
            self.de_lock.release()
        if self.en_lock.locked():
            self.en_lock.release()
        return val

        

    def size(self) -> int:
        return self.count
        