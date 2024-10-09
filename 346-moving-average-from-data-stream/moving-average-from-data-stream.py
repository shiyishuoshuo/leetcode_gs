class MovingAverage:

    def __init__(self, size: int):
        self.total = 0
        self.size = size
        self.q = deque()
        

    def next(self, val: int) -> float:
        self.total += val
        self.q.append(val)
        if self.q and len(self.q) > self.size:
            self.total -= self.q[0]
            self.q.popleft()
        
        return self.total / len(self.q)

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)