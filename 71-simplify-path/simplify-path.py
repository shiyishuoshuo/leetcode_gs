class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        stk = []

        for portion in paths[1:]:
            if portion == '.' or not portion:
                continue
            elif portion == '..':
                if stk:
                    stk.pop()
            else:
                stk.append(portion)
        
        return '/' + "/".join(stk)
        