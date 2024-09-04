class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = Counter(s)
        for c in t:
            if c not in s:
                return False
            count_s[c] -= 1

        return not any([ True for cnt in count_s.values() if cnt != 0])
        





        