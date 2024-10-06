class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        res = [''] * numRows
        step = -1
        cur_row = 0

        for char in s:
            res[cur_row] += char
            if cur_row == 0 or cur_row == numRows - 1:
                step = -step
            cur_row += step
        
        return ''.join(res)

        