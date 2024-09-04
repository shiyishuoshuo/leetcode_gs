class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        double_s = s + s

        index_s = double_s.index(s, 1)

        return index_s < len(s)

        