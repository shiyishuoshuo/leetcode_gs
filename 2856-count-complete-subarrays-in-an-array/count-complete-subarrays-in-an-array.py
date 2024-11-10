class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique_count = len(set(nums))
        windows = Counter()
        left, right = 0, 0
        res = 0

        while right < len(nums):
            d = nums[right]
            windows[d] += 1
            right += 1

            while left < right and unique_count == len(windows):
                res += len(nums) - right + 1
                c = nums[left]
                windows[c] -= 1
                if windows[c] == 0:
                    windows.pop(c)
                left += 1
            
        
        return res