class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        output = [0] * n
        stk = []

        for i in range(n - 1, -1, -1):

            while stk and stk[-1] < heights[i]:
                output[i] += 1
                stk.pop()

            if stk:
                output[i] += 1
            
            stk.append(heights[i])
        
        return output

        