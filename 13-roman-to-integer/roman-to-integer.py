class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        prev, res =  map[s[-1]] , map[s[-1]]

        for i in range(n - 2, -1, -1):
            current = map[s[i]]
            if current < prev:
                res -= current
            else:
                res += current
            prev = current

        return res

