class Solution:
    def countBits(self, n: int) -> List[int]:
        offset = 1
        dp = [0] * (n + 1)

        for val in range(1, n + 1):
            if val == offset * 2:
                offset = offset * 2
            dp[val] = dp[val - offset] + 1
        
        return dp



        