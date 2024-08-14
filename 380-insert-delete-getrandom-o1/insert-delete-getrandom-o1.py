class RandomizedSet:

    def __init__(self):
        self.numbers = []
        self.valToIndex = {}

    def insert(self, val: int) -> bool:
        if val in self.valToIndex:
            return False
        self.valToIndex[val] = len(self.numbers)
        self.numbers.append(val)
        return True

    def remove(self, val: int) -> bool:
        n = len(self.numbers)
        if val not in self.valToIndex:
            return False
        index_to_remove = self.valToIndex[val]
        last_element = self.numbers[-1]
        if index_to_remove == n - 1:
            self.removeLastElement(val)
            return True
        self.numbers[index_to_remove] = last_element
        self.valToIndex[last_element] = index_to_remove
        self.removeLastElement(val)
        return True

    def removeLastElement(self, lastVal: int):
        self.numbers.pop()
        del self.valToIndex[lastVal]

    def getRandom(self) -> int:
        return self.numbers[randint(0, len(self.numbers) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
