class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh_oranges = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1

        minutes = 0

        while q and fresh_oranges > 0:
            minutes += 1
            for level in range(len(q)):
                x, y = q.popleft()

                for delta_x, delta_y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    r, c = x + delta_x, y + delta_y
                    if r not in range(rows) or c not in range(cols) or grid[r][c] != 1:
                        continue
                    fresh_oranges -= 1
                    grid[r][c] = 2
                    q.append((r, c))

        return minutes if fresh_oranges == 0 else -1
