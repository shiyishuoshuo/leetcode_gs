class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        min_sum, max_sum = nums[0], nums[0]
        cur_min, cur_max = nums[0], nums[0]
        total_sum = nums[0]

        for i in range(1, len(nums)):
            cur_max = max(nums[i], cur_max + nums[i])
            cur_min = min(nums[i], cur_min + nums[i])
            max_sum = max(max_sum, cur_max)
            min_sum = min(min_sum, cur_min)
            total_sum += nums[i]
        
        if max_sum <= 0:
            return max_sum
        
        return max(max_sum, total_sum - min_sum)
        