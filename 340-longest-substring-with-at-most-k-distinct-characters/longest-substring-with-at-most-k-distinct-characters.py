class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        windows = Counter()
        left, right = 0, 0
        longest_len = 0

        while right < len(s):
            d = s[right]
            right += 1

            windows[d] += 1

            while left < right and len(windows) > k:
                c = s[left]
                if c in windows:
                    windows[c] -= 1
                    if windows[c] == 0:
                        del windows[c]
                left += 1
            longest_len = max(longest_len, right - left)

        return longest_len

        