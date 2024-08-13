class Solution:

    def __init__(self, w: List[int]):
        n = len(w)
        self.prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + w[i - 1]
        

    def pickIndex(self) -> int:
        # here I am blocked to where to find the target value so the target value range should be [1, prefix_sum[n - 1]]
        n = len(self.prefix_sum)
        target = randint(1, self.prefix_sum[n - 1])
        low, high = 0, len(self.prefix_sum)
        while low < high:
            mid = (high - low) // 2 + low
            if self.prefix_sum[mid] == target:
                high = mid
            elif self.prefix_sum[mid] < target:
                low = mid + 1
            elif self.prefix_sum[mid] > target:
                high = mid
        return low - 1

            
        
    

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()