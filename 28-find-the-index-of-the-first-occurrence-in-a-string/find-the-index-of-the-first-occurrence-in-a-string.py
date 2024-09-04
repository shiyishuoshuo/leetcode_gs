class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m , n = len(haystack), len(needle)

        for window_start in range(m - n + 1):
            for j in range(n):
                if haystack[window_start + j] != needle[j]:
                    break
                if j == n - 1:
                    return window_start
        
        return -1


