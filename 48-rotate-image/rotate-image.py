class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(i + 1, col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        def reverseRow(row: List[int]):
            i, j = 0, len(row) - 1
            while i < j:
                row[i], row[j] = row[j], row[i]
                i += 1
                j -= 1
                 
        for i in range(row):
            reverseRow(matrix[i])
        