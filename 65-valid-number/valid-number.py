class Solution:
    def isNumber(self, s: str) -> bool:
        n = len(s)
        index = 0

        if s[index] in '+-':
            index += 1
            
        if index == n:
            return False

        if s[index] == '.' and (index + 1 == n or s[index + 1] in 'eE'):
            return False

        dot_count, exp_count = 0, 0

        while index < n:
            if s[index] == '.':
                if exp_count or dot_count:
                    return False
                dot_count += 1
            elif s[index] in 'eE':
                if exp_count or index == 0 or index == n - 1 or (index >= 1 and s[index - 1] in '+-'):
                    return False
                exp_count += 1
                if s[index + 1] in '+-':
                    index += 1
                    if index == n - 1:
                        return False
            elif not s[index].isdigit():
                return False
            
            index += 1

        return True
                
        