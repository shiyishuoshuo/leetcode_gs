class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter_s = Counter(s)
        counter_t = Counter(t)

        for key, cnt in counter_t.items():
            if key not in counter_s:
                return key
            if cnt == counter_s[key] + 1:
                return key
        
        return ''