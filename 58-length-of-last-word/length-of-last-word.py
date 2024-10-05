class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        res = 0
        first_non_empty_index = n - 1

        while first_non_empty_index >= 0 and s[first_non_empty_index] == ' ':
            first_non_empty_index -= 1
        
        if first_non_empty_index < 0:
            return 0

        while first_non_empty_index >= 0 and s[first_non_empty_index] != ' ':
            first_non_empty_index -= 1
            res += 1
        
        return res
        