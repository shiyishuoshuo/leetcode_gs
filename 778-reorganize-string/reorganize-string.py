class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)

        counters = Counter(s)
        max_freq = max(counters.values())
        if max_freq > (n + 1) // 2:
            return ''
        
        res = [None] * n
        index = 0
        for char, freq in counters.most_common():
            while freq:
                res[index] = char
                freq -= 1
                index += 2
                if index > n - 1:
                    index = 1
        return ''.join(res)



        