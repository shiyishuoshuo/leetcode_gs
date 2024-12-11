class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] * (n + 1)

        for i in range(1, n + 1):
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1]
        
        m = len(prefixSum)
        print(f'prefixSum array: ${prefixSum}')
        for j in range(1, m):
            if prefixSum[j - 1] == prefixSum[m - 1] - prefixSum[j]:
                return j - 1

        return - 1
        