class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for operation in operations:
            if operation not in ['C', 'D', '+']:
                res.append(int(operation))
            else:
                if operation == 'C':
                    res.pop()
                if operation == 'D':
                    res.append(res[-1] * 2)
                if operation == '+':
                    temp_sum = res[-1] + res[-2]
                    res.append(temp_sum)
        
        return sum(res)
            
        