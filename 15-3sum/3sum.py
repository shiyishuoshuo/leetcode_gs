class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)

        def nSum(start: int, target: int, n: int) -> List[List[int]]:
            res = []
            if n < 2:
                return res
            elif n == 2:
                low, high = start, length - 1
                while low < high:
                    two_sum = nums[low] + nums[high]
                    if two_sum == target:
                        res.append([nums[low], nums[high]])
                        low += 1
                        high -= 1
                        while low < high and nums[low] == nums[low - 1]:
                            low += 1
                        while low < high and nums[high] == nums[high + 1]:
                            high -= 1
                    elif two_sum < target:
                        low += 1
                    elif two_sum > target:
                        high -= 1
                return res
            elif n > 2:
                for i in range(start, length):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    other_sum = nSum(i + 1, target - nums[i], n - 1)
                    for pair in other_sum:
                        pair.append(nums[i])
                        res.append(pair)

                return res

        return nSum(0, 0, 3)
