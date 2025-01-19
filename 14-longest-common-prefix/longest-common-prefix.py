class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                cur = strs[j]
                if i == len(cur) or cur[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res
        