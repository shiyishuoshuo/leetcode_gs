class RecentCounter:

    def __init__(self):
        self.total = 0
        self.q = deque()
        

    def ping(self, t: int) -> int:
        while self.q:
            if t - 3000 > self.q[0]:
                self.total -= 1
                self.q.popleft()
            else:
                break
        self.q.append(t)
        self.total += 1
        return self.total
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)