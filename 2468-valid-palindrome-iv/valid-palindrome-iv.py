class Solution:
    def makePalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        count = 0
        while i < j:
            if s[i] != s[j]:
                count += 1
            i += 1
            j -= 1
        
        if count <= 2:
            return True
        
        return False

        