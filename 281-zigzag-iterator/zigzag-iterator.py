class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vectors = [v1, v2]
        self.p_elem = 0   # pointer to the index of element
        self.p_vec = 0    # pointer to the vector
        # variables for hasNext() function
        self.total_num = len(v1) + len(v2)
        self.output_count = 0

    def next(self) -> int:
        # Attempt to get the next element from the current vector
        curr_vec = self.vectors[self.p_vec]
        if self.p_elem < len(curr_vec):
            ret = curr_vec[self.p_elem]
            self.output_count += 1
            # Prepare pointers for next call
            self.p_vec = (self.p_vec + 1) % len(self.vectors)
            if self.p_vec == 0:
                self.p_elem += 1
            return ret
        else:
            # Move to the next vector and retry
            self.p_vec = (self.p_vec + 1) % len(self.vectors)
            if self.p_vec == 0:
                self.p_elem += 1
            return self.next()  # Recursive call to handle skipping empty indices

    def hasNext(self) -> bool:
        return self.output_count < self.total_num
