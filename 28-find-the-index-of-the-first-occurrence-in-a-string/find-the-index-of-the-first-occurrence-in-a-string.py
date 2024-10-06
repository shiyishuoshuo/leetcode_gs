class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(needle), len(haystack)

        for i in range(n - m + 1):
            if haystack[i: i + m] == needle:
                return i
        return - 1