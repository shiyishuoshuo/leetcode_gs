class Solution:
    def jump(self, nums: List[int]) -> int:
        furthest, last, jumps = 0, 0, 0
        for index, jump in enumerate(nums[:-1]):
            furthest = max(furthest, index + jump)
            if index == last:
                jumps += 1
                last = furthest
        return jumps
