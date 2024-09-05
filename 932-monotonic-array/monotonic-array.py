class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        
        index, diff = 0, 0
        while index < n - 1 and nums[index] == nums[index + 1]:
            index += 1
        if index == n - 1:
            return True
        diff = nums[index + 1] - nums[index]

        for i in range(index, n - 1):
            if diff > 0:
                if nums[i + 1] - nums[i] < 0:
                    return False
            else:
                if nums[i + 1] - nums[i] > 0:
                    return False
        
        return True
                
        