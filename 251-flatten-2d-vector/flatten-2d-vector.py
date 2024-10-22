class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.v = vec
        self.outer = 0
        self.inner = 0

    def next(self) -> int:
        self.forward()
        res = self.v[self.outer][self.inner]
        self.inner += 1
        return res

    def hasNext(self) -> bool:
        self.forward()
        return self.outer < len(self.v)

    def forward(self) -> None:
        while self.outer < len(self.v) and self.inner == len(self.v[self.outer]):
            self.outer += 1
            self.inner = 0


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
