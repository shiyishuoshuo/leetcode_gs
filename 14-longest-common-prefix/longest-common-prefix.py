class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        strs = sorted(strs, key = lambda x: len(x))

        if len(strs) == 1:
            return strs[0]
        
        word = strs[0]

        res = ''

        i = 1
        outer_loop_done = False
        while i < len(word) + 1:
            prefix = word[0:i]

            for j in range(1, n):
                if prefix not in strs[j][0:i]:
                    outer_loop_done = True
                    break
            if outer_loop_done:
                break
            res = prefix
            i += 1
        
        return res

        