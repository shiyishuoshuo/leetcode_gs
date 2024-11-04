class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        res = -1
        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum < k:
                res = max(res, two_sum)
                left += 1
            else:
                right -= 1
        return res