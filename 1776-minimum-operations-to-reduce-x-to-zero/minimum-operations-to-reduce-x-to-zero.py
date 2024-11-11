class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        sum_nums = sum(nums)
        target = sum_nums - x
        res = -1
        left, right = 0, 0
        nums_length, cur_sum = len(nums), 0

        while right < nums_length:
            cur = nums[right]
            cur_sum += cur
            right += 1

            while left < right and target < cur_sum:
                c = nums[left]
                cur_sum -= c 
                left += 1
            if cur_sum == target:
                res = max(res, right - left)
            
        return -1 if res == -1 else nums_length - res

        