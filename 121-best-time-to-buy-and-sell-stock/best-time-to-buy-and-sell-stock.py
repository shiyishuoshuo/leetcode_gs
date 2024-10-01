class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, min_profit = 0, float('inf')
        for price in prices:
            min_profit = min(min_profit, price)
            profit = max(profit, price - min_profit)
        
        return profit
        