class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 0:
            return False
        
        if n == 1:
            return True

        def next(n: int) -> int:
            output = 0
            while n:
                n, digit = divmod(n, 10)
                output += digit ** 2
            return output

        slow, fast = n, next(n)
        while fast != 1 and slow != fast:
            slow = next(slow)
            fast = next(next(fast))
        return fast == 1
        