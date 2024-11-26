class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # sorted(piles)
        size = len(piles)
        left, right = 1, 1000000000

        while left <= right:
            mid = left + (right - left) // 2
            if(self.canEat(piles, mid, h)):
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    def canEat(self, piles: List[int], k: int, h: int) -> bool:
        hours = 0
        for pile in piles:
            hours += pile // k
            if pile % k > 0:
                hours += 1
        return hours <= h