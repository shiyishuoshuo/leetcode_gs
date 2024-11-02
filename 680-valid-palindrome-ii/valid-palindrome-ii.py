class Solution:
    def validPalindrome(self, s: str) -> bool:
        i , j = 0, len(s) - 1
        
        def isPalindrome(x:int, y:int) -> bool:
            
            while x < y:
                if s[x] != s[y]:
                    return False
                x += 1
                y -= 1
            return True

        while i < j:
            if s[i] != s[j]:
                return isPalindrome(i + 1, j) or isPalindrome(i, j - 1)
            
            i += 1
            j -= 1
        
        return True
        