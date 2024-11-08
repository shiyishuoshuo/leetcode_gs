class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            cur = min(height[left], height[right]) * (right - left)
            res = max(cur, res)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return res
        