class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        left, right = 0, row * col - 1

        while left <= right:
            mid_index = (right - left) // 2 + left
            print(f'left: {left}, right: {right}, mid_index: {mid_index}, new_mid_x: {mid_index // row}, new_mid_y": {mid_index % row}')
            mid_val = matrix[mid_index // col][mid_index % col]
            if mid_val == target:
                return True
            elif mid_val > target:
                right = mid_index - 1
            else:
                left = mid_index + 1
        
        return False