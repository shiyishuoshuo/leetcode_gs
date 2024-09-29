class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vectors = [v1, v2]
        self.queue = deque()
        for index, vector in enumerate(self.vectors):
            if len(vector) > 0:
                self.queue.append((index, 0))

        

    def next(self) -> int:

        if self.queue:
            vec_index, elm_index = self.queue.popleft()
            next_index = elm_index + 1
            if next_index < len(self.vectors[vec_index]):
                self.queue.append((vec_index, next_index))
            return self.vectors[vec_index][elm_index]
        

    def hasNext(self) -> bool:
        return len(self.queue) > 0
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())