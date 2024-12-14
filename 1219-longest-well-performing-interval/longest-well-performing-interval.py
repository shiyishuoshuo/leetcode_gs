class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        prefixSum = 0
        sumToIndex = defaultdict(int)
        res = 0
        for i in range(n):
            prefixSum += (1 if hours[i] > 8 else -1)
            if prefixSum not in sumToIndex:
                sumToIndex[prefixSum] = i
            if prefixSum > 0:
                res = max(res, i + 1)
            else:
                if prefixSum - 1 in sumToIndex:
                    j = sumToIndex[prefixSum - 1]
                    res = max(res, i - j)
        return res

        