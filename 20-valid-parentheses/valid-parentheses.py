class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {')':'(', ']':'[', '}':'{'}
        stk = []

        for c in s:
            if c in ['{', '[', '(']:
                stk.append(c)
            else:
                if stk and c in parentheses_map and parentheses_map[c] == stk[-1]:
                    stk.pop()
                else:
                    return False
        
        return not stk
        