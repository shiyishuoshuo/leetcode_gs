class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0
        for index, number_of_jumps in enumerate(nums):
            if furthest < index:
                return False
            furthest = max(furthest, index + number_of_jumps)
        
        return True
        