class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        sign = 1
        index, n = 0, len(s)
        while index < n and s[index] == ' ':
            index += 1
        if index == n:
            return 0
        
        if index < n:
            if s[index] == '-':
                sign *= -1
                index += 1
            elif s[index] == '+':
                index += 1

        while index < n and s[index] == '0':
            index += 1
        if index == n:
            return 0

        while index < n and '0'<= s[index] <='9':
            res = res * 10 + int(s[index])
            if sign == 1 and res >= 2**31:
                return 2**31 - 1
            elif sign == -1 and abs(res) > 2**31:
                return -2**31
            index += 1

        
        
        return res if sign == 1 else -res
        
        
        