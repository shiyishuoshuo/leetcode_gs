class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        len_s, len_g = len(s), len(goal)
        if len_s != len_g:
            return False
        
        count_s, count_g = Counter(s), Counter(goal)

        if count_s != count_g:
            return False

        diff_count = sum([1 for i in range(len_s) if s[i] != goal[i]])

        return diff_count == 2 or (diff_count == 0 and any(val > 1 for val in count_s.values()))
        