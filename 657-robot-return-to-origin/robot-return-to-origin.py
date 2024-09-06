class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # count of L is equal to count of R 
        # and count of U is equal to count of D
        move_count = Counter(moves)

        for move, cnt in move_count.items():
            if move == 'L':
                if 'R' not in move_count or move_count['R'] != cnt:
                    return False
            if move == 'D':
                if 'U' not in move_count or move_count['U'] != cnt:
                    return False
            if move == 'R':
                if 'L' not in move_count or move_count['L'] != cnt:
                    return False
            if move == 'U':
                if 'D' not in move_count or move_count['D'] != cnt:
                    return False
        
        return True

                

        