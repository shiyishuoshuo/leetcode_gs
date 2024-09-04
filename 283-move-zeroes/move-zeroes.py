class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start_zero, index = 0, 0

        while index < len(nums):
            if nums[index] != 0:
                nums[index], nums[start_zero] = nums[start_zero], nums[index]
                start_zero += 1
            index += 1
    