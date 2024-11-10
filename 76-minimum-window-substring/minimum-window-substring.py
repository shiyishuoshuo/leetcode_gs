class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = Counter()
        need = Counter(t)
        left, right = 0, 0
        valid = 0
        start, length = 0, float('inf')

        while right < len(s):
            d = s[right]
            right += 1
            if d in need:
                window[d] += 1
                if window[d] == need[d]:
                    valid += 1
            
            while left < right and valid == len(need):
                c = s[left]
                if right - left < length:
                    start = left
                    length = right - left
                left += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
        
        return "" if length == float('inf') else s[start:start + length]
