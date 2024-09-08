class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        i, j = m - 1, n - 1
        carry = 0
        res = []
        while i >= 0 or j >=0:
            digit_a = a[i] if i >= 0 else '0'
            digit_b = b[j] if j >= 0 else '0'
            res.append(int(digit_a) ^ int(digit_b) ^ carry)
            carry = int(digit_a) & int(digit_b) or (carry & int(digit_a)) or (carry & int(digit_b))
            i -= 1
            j -= 1

        if carry > 0:
            res.append(1)

        return "".join([str(c) for c in res[::-1]])


        