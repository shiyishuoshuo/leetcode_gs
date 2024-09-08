class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        num_five, num_ten = 0, 0

        for bill in bills:
            if bill == 5:
                num_five += 1
            if bill == 10:
                if num_five < 1:
                    return False
                num_ten += 1
                num_five -= 1
            if bill == 20:
                if num_ten >= 1 and num_five >= 1:
                    num_ten -= 1
                    num_five -= 1
                elif num_five >= 3:
                    num_five -= 3
                else:
                    return False
        
        return True
        