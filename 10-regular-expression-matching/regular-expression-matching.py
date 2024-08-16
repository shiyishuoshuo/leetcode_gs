class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)

        memo = [[-1] * p_len for _ in range(s_len)]

        def dp(i: int, s: str, j: int, p: str) -> bool:
            if j == p_len:
                return i == s_len

            if i == s_len:
                if (p_len - j) % 2 == 1:
                    return False
                for k in range(j, p_len, 2):
                    if p[k + 1] != "*":
                        return False
                return True

            if memo[i][j] != -1:
                return memo[i][j] == 1

            res = False

            if p[j] in [s[i], "."]:
                if j < p_len - 1 and p[j + 1] == "*":
                    res = dp(i, s, j + 2, p) or dp(i + 1, s, j, p)
                else:
                    res = dp(i + 1, s, j + 1, p)
            else:
                if j < p_len - 1 and p[j + 1] == "*":
                    res = dp(i, s, j + 2, p)
                else:
                    res = False

            memo[i][j] = 1 if res else 0
            return res

        return dp(0, s, 0, p)
