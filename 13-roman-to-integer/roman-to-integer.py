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
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        i, res = 0 , 0

        while i < n:
            if i < n - 1 and s[i:i+2] in map:
                res += map[s[i:i+2]]
                i += 2
            else:
                res += map[s[i]]
                i += 1

        return res

