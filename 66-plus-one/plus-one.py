class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 0

        for i in range(len(digits) - 1, -1, -1):
            digit_sum = 0
            if i == len(digits) - 1:
                digit_sum = digits[i] + 1 + carry
            else:
                digit_sum = digits[i] + carry
            
            carry, digits[i] = divmod(digit_sum, 10)
        
        if carry > 0:
            return [1] + digits
        
        return digits

        