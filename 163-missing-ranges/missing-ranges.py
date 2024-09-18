class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        if len(nums) == 0:
            res.append([lower, upper])
            return res
        
        if lower < nums[0]:
            res.append([lower, nums[0] - 1])
        
        cur = 0
        while cur < len(nums) - 1:
            start, end = nums[cur], nums[cur + 1]
            if end - start > 1:
                res.append([start + 1, end - 1])
            cur += 1
        
        if nums[-1] < upper:
            res.append([nums[-1] + 1, upper])

        return res

        
        