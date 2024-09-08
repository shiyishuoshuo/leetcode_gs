class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        prev_one, prev_two = nums[0], nums[1]
        res = 0
        print(f'nums: {nums}')
        for i in range(2, len(nums)):
            cur = nums[i]
            if prev_one + prev_two > cur:
                res = max(res, cur + prev_one + prev_two)
            prev_one = prev_two
            prev_two = cur

        return res
