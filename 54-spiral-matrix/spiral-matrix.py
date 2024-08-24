class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        upper_bound, lower_bound = 0, row - 1
        left_bound, right_bound = 0, col - 1
        res = []

        while len(res) < row * col:

            # top left to right 
            if upper_bound <= lower_bound:
                for i in range(left_bound, right_bound + 1):
                    res.append(matrix[upper_bound][i])
                upper_bound += 1
            
            if left_bound <= right_bound:
                for i in range(upper_bound, lower_bound + 1):
                    res.append(matrix[i][right_bound])
                right_bound -= 1

            if upper_bound <= lower_bound:
                for j in range(right_bound, left_bound - 1, -1):
                    res.append(matrix[lower_bound][j])
                lower_bound -= 1

            if left_bound <= right_bound:
                for i in range(lower_bound, upper_bound - 1, -1):
                    res.append(matrix[i][left_bound])
                left_bound += 1
        
        return res



        