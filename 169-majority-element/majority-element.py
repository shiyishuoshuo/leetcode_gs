class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target, count = 0, 0

        for num in nums:
            if count == 0:
                target = num
                count = 1
            elif num == target:
                count += 1
            else:
                count -= 1
        
        return target
        