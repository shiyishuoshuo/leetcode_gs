class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        
        while fast < len(nums):
            if fast > 0 and nums[fast] != nums[fast - 1]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        
        return slow + 1
        