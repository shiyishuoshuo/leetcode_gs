class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stk = []
        output = [0] * n

        for i in range(n - 1, -1, -1):
            while stk and temperatures[i] >= temperatures[stk[-1]]:
                stk.pop()
            output[i] = 0 if not stk else stk[-1] - i
            stk.append(i)
        
        return output
        