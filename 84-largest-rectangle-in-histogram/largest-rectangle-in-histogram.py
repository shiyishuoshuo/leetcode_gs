class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area, n = 0, len(heights)
        stk = []

        for i in range(n + 1):
            while stk and (i == n or heights[i] < heights[stk[-1]]):
                height = heights[stk.pop()]
                width = i - 1 - stk[-1] if stk else i
                max_area = max(max_area, height * width)          
            stk.append(i)

        return max_area


        
        