class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        remaining_digits_count = len(num) - k

        for c in num:

            while stk and k > 0 and c < stk[-1]:
                stk.pop()
                k -= 1
            
            stk.append(c)

        final_number = ''.join(stk[:remaining_digits_count])

        return final_number.lstrip('0') or '0'

        