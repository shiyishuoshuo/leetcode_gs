class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vectors = [v1, v2]
        self.index = 0
        self.current = 0
        self.size = 2
        self.total_number = len(v1) + len(v2)
        self.output_count = 0
        

    def next(self) -> int:
        vector = self.vectors[self.current]
        if self.index < len(vector):
            res = vector[self.index]
            self.output_count += 1
            self.current = (self.current + 1) % self.size
            if self.current == 0:
                self.index += 1
            return res
        else:
            self.current = (self.current + 1) % self.size
            if self.current == 0:
                self.index += 1
            return self.next()
        
        

    def hasNext(self) -> bool:
        return self.output_count < self.total_number
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())