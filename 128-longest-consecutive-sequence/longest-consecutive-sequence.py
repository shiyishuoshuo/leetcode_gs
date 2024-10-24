class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence_set = set(nums)
        res = 0

        for num in nums:

            if num - 1 in sequence_set:
                continue

            cur_num = num
            cur_count = 1

            while cur_num + 1 in sequence_set:
                cur_count += 1
                cur_num += 1
            
            res = max(res, cur_count)
        
        return res

        