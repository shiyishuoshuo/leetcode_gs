class FreqStack:

    def __init__(self):
        self.maxFrq = -1
        self.valToFrq = {}
        self.frqToVals = {}
        

    def push(self, val: int) -> None:
        if val not in self.valToFrq:
            self.valToFrq[val] = 0
        self.valToFrq[val] += 1
        frq = self.valToFrq[val]
        self.maxFrq = max(self.maxFrq, frq)
        if frq not in self.frqToVals:
            self.frqToVals[frq] = []
        self.frqToVals[frq].append(val)
        

    def pop(self) -> int:
        stk = self.frqToVals[self.maxFrq]
        output = stk.pop()
        if not stk:
            self.frqToVals.pop(self.maxFrq)
            self.maxFrq -= 1
        self.valToFrq[output] -= 1
        return output
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()