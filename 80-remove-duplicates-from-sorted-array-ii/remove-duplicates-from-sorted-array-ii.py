class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        count = 0
        
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                count = 0
            elif slow < fast and count < 2:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
            count += 1
        
        return slow + 1
        