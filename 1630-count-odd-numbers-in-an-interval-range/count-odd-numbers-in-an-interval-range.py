class Solution:
    def countOdds(self, low: int, high: int) -> int:

        diff = (high - low) + 1
        if diff % 2 == 0:
            return diff // 2
        else:
            if high % 2:
                return diff // 2 + 1
            return diff // 2

        return 0
        