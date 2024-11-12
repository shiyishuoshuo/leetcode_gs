class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = Counter()
        s_len = len(s)
        left, right = 0, 0
        res, max_f = 0, 0

        while right < s_len:
            d = s[right]
            window[d] += 1
            max_f = max(max_f, window[d])
            right += 1

            while left < right and right - left - max_f > k:
                c = s[left]
                window[c] -= 1
                if window[c] == 0:
                    del window[c]
                left += 1
            
            res = max(res, right - left)
        
        return res
        