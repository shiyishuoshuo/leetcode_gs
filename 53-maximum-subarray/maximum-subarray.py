class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        @cache
        def maxSubArrayHelper(index: int) -> int:
            if index - 1 < 0:
                return nums[index]
            return max(maxSubArrayHelper(index - 1) + nums[index], nums[index])

        res, n = nums[0], len(nums)

        for i in range(n - 1, -1, -1):
            res = max(res, maxSubArrayHelper(i))
        return res
        
        
        