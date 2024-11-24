class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = Counter()
        need = Counter(t)
        left, right = 0, 0
        valid = 0
        start, length = 0, float('inf')
        filtered_s = []

        for (i, c) in enumerate(s):
            if c in need:
                filtered_s.append((i, c))

        while right < len(filtered_s):
            d = filtered_s[right][1]
            right += 1
            window[d] += 1
            if window[d] == need[d]:
                valid += 1
            
            while left < right and valid == len(need):
                c = filtered_s[left][1]
                print(f'right: {right} and left: {left} and size of filtered_s is {len(filtered_s)}')
                if filtered_s[right - 1][0] - filtered_s[left][0] < length:
                    start = filtered_s[left][0]
                    length = filtered_s[right - 1][0] - filtered_s[left][0]
                left += 1

                if window[c] == need[c]:
                    valid -= 1
                window[c] -= 1
        
        return "" if length == float('inf') else s[start:start + length + 1]
