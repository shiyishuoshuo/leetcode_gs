class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return

        def swap(nums, i:int, j:int) -> None:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        def rotateHelper(nums, low:int, high:int) -> None:
            while low < high:
                swap(nums, low, high)
                low += 1
                high -= 1
        n = len(nums)

        k = k % n
        rotateHelper(nums, 0, n - 1)
        rotateHelper(nums, 0, (k - 1))
        rotateHelper(nums, k, n - 1)


        
        