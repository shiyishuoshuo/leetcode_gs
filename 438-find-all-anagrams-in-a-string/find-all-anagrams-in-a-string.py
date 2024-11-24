class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_counter, p_counter = Counter(), Counter(p)
        left, right = 0, 0
        s_len, p_len = len(s), len(p)
        anagram_results = []

        while right < s_len:
            d = s[right]
            s_counter[d] += 1
            right += 1

            if left < right and (right - left - 1) == p_len:
                c = s[left]
                if c in s_counter:
                    s_counter[c] -= 1
                    if s_counter[c] == 0:
                        del s_counter[c]
                left += 1
            
            if s_counter == p_counter:
                anagram_results.append(left)
            

        return anagram_results
            

