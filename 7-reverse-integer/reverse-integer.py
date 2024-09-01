class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2 ** 31 - 1
        is_negative = False
        if x < 0:
            is_negative = True
            x = x * -1
        
        res = 0
        
        while x:
            next_x, digit = divmod(x, 10)

            if (res > MAX // 10) or (res == MAX // 10 and digit > MAX % 10):
                return 0

            res = (res * 10) + digit 
            x = next_x
        
        return res * -1 if is_negative else res
        