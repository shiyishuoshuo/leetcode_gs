class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = Counter(s)
        for c in t:
            count_s[c] -= 1
            if count_s[c] < 0:
                return False

        return True
        





        