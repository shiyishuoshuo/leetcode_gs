class DetectSquares:

    def __init__(self):
        self.pointCounter = defaultdict(int)
        self.pointers = []
        

    def add(self, point: List[int]) -> None:
        self.pointCounter[tuple(point)] += 1
        self.pointers.append(tuple(point))
        

    def count(self, point: List[int]) -> int:
        res = 0
        qx, qy = point
        for (x, y) in self.pointers:
            if abs(x - qx) == 0 or abs(qx - x) != abs(qy - y):
                continue
            res += self.pointCounter[(qx, y)] * self.pointCounter[(x, qy)]
        return res
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)