class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEat(piles: List[int], speed:int, h:int) -> bool:
            hours = 0
            for pile in piles:
                hours += pile // speed
                if pile % speed > 0:
                    hours += 1
            return hours <= h
        
        n = len(piles)
        left, right = 1, max(piles)

        while left <= right:
            mid = (right - left) // 2 + left
            if canEat(piles, mid, h):
                right = mid - 1
            else:
                left = mid + 1
        return left

        

