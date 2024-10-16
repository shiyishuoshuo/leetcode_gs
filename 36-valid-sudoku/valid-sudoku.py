class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        r, c = len(board), len(board[0])
        row = [0] * N
        col = [0] * N
        cube = [0] * N

        for i in range(N):
            for j in range(N):
                if board[i][j] == '.':
                    continue
                    
                pos = int(board[i][j]) - 1

                if row[i] & (1 << pos):
                    return False 
                row[i] |= (1 << pos)

                if col[j] & (1 << pos):
                    return False 
                col[j] |= (1 << pos)

                idx = (i // 3) * 3 + j // 3
                if cube[idx] & (1 << pos):
                    return False 
                cube[idx] |= (1 << pos)

        return True


        
        