class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF; 
        a, b = a & MASK, b & MASK

        while b:
            carry = (a & b) << 1 & MASK
            a , b = a ^ b , carry
        
        if a < 0x80000000:
            return a
        
        return ~(a ^ MASK)


        