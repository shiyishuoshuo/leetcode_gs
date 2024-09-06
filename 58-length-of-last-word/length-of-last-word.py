class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        first_non_empty_index = n - 1
        res = 0

        while first_non_empty_index > -1:
            if s[first_non_empty_index] != ' ':
                break
            first_non_empty_index -= 1

        while first_non_empty_index > -1:
            if s[first_non_empty_index] == ' ':
                break
            first_non_empty_index -= 1
            res += 1
        
        return res
        