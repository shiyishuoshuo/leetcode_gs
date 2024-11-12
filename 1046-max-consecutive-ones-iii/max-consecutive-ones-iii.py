class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        num_len = len(nums)
        count_one = 0
        left, right = 0, 0
        res = 0

        while right < num_len:
            cur = nums[right]
            if cur == 1:
                count_one += 1
            right += 1

            while left < right and right - left - count_one > k:
                c = nums[left]
                if c == 1:
                    count_one -= 1
                left += 1
            
            res = max(res, right - left)
        
        return res
        