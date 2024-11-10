class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        chars = Counter()
        res = 0

        while right < len(s):
            d = s[right]
            chars[d] += 1
            right += 1

            while left < right and chars[d] > 1:
                l =s[left]
                chars[l] -= 1
                left += 1
            res = max(res, (right - left))
        
        return res

            
            
                
            
        