class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        res = [0] * (n1 + n2)

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 -1, -1, -1):
                res[i + j + 1] += int(num1[i]) * int(num2[j])
                carry, res[i + j + 1] = divmod(res[i + j + 1], 10)
                res[i + j] += carry
        
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1
        
        str_res = ''.join(str(x) for x in res[i:])

        return '0' if not str_res else str_res

        