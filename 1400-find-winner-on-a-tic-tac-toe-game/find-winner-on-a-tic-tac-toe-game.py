class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        row = [0] * 3
        col = [0] * 3
        diag, anti_diag = 0, 0

        for i in range(len(moves) - 1, -1, -2):
            m, n = moves[i]

            row[m] += 1
            col[n] += 1

            if m == n:
                diag += 1

            if m + n == 2:
                anti_diag += 1

            if any([val == 3 for val in row]) or \
                any([val == 3 for val in col]) or \
                diag == 3 or anti_diag == 3:
                return 'B' if i % 2 else 'A'
        
        return 'Draw' if len(moves) == 9 else 'Pending'
        

        