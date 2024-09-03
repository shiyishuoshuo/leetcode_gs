class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s and len(t) == 1:
            return t
        
        s, t = sorted(s), sorted(t)
        i,j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                return t[j]
            i += 1
            j += 1
        return t[j]